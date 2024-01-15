#!/usr/bin/env python3
"""
Created on
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
