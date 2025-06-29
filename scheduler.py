from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from config import TIMEZONE
from pytz import timezone

async def schedule_jobs(job_func):
    scheduler = AsyncIOScheduler(timezone=timezone(TIMEZONE))
    scheduler.add_job(job_func, CronTrigger(hour=11, minute=0))
    scheduler.add_job(job_func, CronTrigger(hour=20, minute=0))
    scheduler.start()