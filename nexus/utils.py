import sys
import time
import signal
import asyncio
from typing import Dict
from pathlib import Path
from typing import Optional
from loguru import logger
from datetime import timezone, datetime


class LiveClock:
    def __init__(self):
        pass

    def timestamp(self):
        return time.time()

    def timestamp_ms(self):
        return time.time_ns() // 1_000_000

    def timestamp_ns(self):
        return time.time_ns()

    def utc_now(self):
        return datetime.now(timezone.utc)

    def iso_now(self, timespec="milliseconds"):
        return self.utc_now().isoformat(timespec=timespec).replace("+00:00", "Z")


class Log:
    _initialized = False

    @staticmethod
    def setup_logger(
        log_path: Optional[str] = None,
        log_level: str = "INFO",
        rotation: str = "20 MB",
        retention: str = "10 days",
    ):
        if Log._initialized:
            return

        logger.remove()

        # 添加标准输出处理器，使用带颜色的自定义格式
        logger.add(
            sink=sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}:{extra[classname]}:{function}:{line}</cyan> - <level>{message}</level>",
            level=log_level,
            colorize=True,
            enqueue=True,
        )

        if log_path:
            log_dir = Path(log_path)
            log_dir.mkdir(parents=True, exist_ok=True)

            # 文件输出不需要颜色标签
            logger.add(
                sink=str(log_dir / "app.log"),
                format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{extra[classname]}:{function}:{line} - {message}",
                level=log_level,
                rotation=rotation,
                retention=retention,
                compression="zip",
                enqueue=True,
                colorize=True,
            )

        Log._initialized = True

    @staticmethod
    def get_logger(classname: str):
        """获取带有类名上下文的logger"""
        return logger.bind(classname=classname)


class TaskManager:
    def __init__(self, loop: asyncio.AbstractEventLoop, enable_signal_handlers: bool = True):
        self._log = Log.get_logger(type(self).__name__, level="DEBUG", flush=True)
        self._tasks: Dict[str, asyncio.Task] = {}
        self._shutdown_event = asyncio.Event()
        self._loop = loop
        if enable_signal_handlers:
            self._setup_signal_handlers()

    def _setup_signal_handlers(self):
        try:
            for sig in (signal.SIGINT, signal.SIGTERM):
                self._loop.add_signal_handler(sig, lambda: self.create_task(self._shutdown()))
        except NotImplementedError:
            self._log.warning("Signal handlers not supported on this platform")

    async def _shutdown(self):
        self._shutdown_event.set()
        self._log.debug("Shutdown signal received, cleaning up...")

    def create_task(self, coro: asyncio.coroutines, name: str = None) -> asyncio.Task:
        task = asyncio.create_task(coro, name=name)
        self._tasks[task.get_name()] = task
        task.add_done_callback(self._handle_task_done)
        return task
    
    def cancel_task(self, name: str) -> bool:
        if name in self._tasks:
            self._tasks[name].cancel()
            return True
        return False

    def _handle_task_done(self, task: asyncio.Task):
        try:
            name = task.get_name()
            self._tasks.pop(name, None)
            task.result()
        except asyncio.CancelledError:
            pass
        except Exception as e:
            self._log.error(f"Error during task done: {e}")
            raise

    async def wait(self):
        try:
            if self._tasks:
                await self._shutdown_event.wait()
                self._log.debug("Shutdown Completed")
        except Exception as e:
            self._log.error(f"Error during wait: {e}")
            raise

    async def cancel(self):
        try:
            for task in self._tasks.values():
                if not task.done():
                    task.cancel()

            if self._tasks:
                results = await asyncio.gather(*self._tasks.values(), return_exceptions=True)

                for result in results:
                    if isinstance(result, Exception) and not isinstance(
                        result, asyncio.CancelledError
                    ):
                        self._log.error(f"Task failed during cancellation: {result}")

        except Exception as e:
            self._log.error(f"Error during cancellation: {e}")
            raise
        finally:
            self._tasks.clear()
