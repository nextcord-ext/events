import asyncio
import nextcord
import datetime
from functools import wraps
from typing import Callable, Optional

SLEEP_FOR = 2.5

from ._events import _ALL


class EventsMixin(nextcord.Client):

    async def on__event(self, event, *args, **kwargs):
        for event_name, event_check in _ALL.items():
            asyncio.ensure_future(event_check(self, event, *args, **kwargs))

    def dispatch(self, event, *args, **kwargs):
        super().dispatch(event, *args, **kwargs)  # type: ignore
        super().dispatch('_event', event, *args, **kwargs)


async def fetch_recent_audit_log_entry(client: nextcord.Client, guild: nextcord.Guild, *, target: nextcord.User = None,
                                       action: nextcord.AuditLogAction = None, retry: int = 0) -> Optional[nextcord.AuditLogEntry]:
    """|coro|
    Attempts to retrieve an recently created :class:`~nextcord.AuditLogEntry` which meets the specified requirements.
    Parameters
    ----------
    client: :class:`~nextcord.Client`
        The nextcord client to make the api calls with.
    guild: :class:`~nextcord.Guild`
        The guild to retrieve the audit log entry from.
    target: Optional[:class:`~nextcord.User`]
        The target to filter with.
    action: Optional[:class:`~nextcord.AuditLogAction`]
        The action to filter with.
    retry: Optional[:class:`int`]
        The number of times fetching an entry should be retried.
        Defaults to 0.
    Raises
    ------
    Forbidden
        You do not have access to the guild's audit log.
    HTTPException
        Fetching the member failed.
    Returns
    --------
    Optional[:class:`~nextcord.AuditLogEntry`]
        The relevant audit log entry if found.
    """
    async for entry in guild.audit_logs(limit=1, action=action):

        delta = datetime.datetime.utcnow() - entry.created_at
        if delta < datetime.timedelta(seconds=10):
            if target is not None and entry.target != target:
                continue

            return entry

    if retry > 0:
        await asyncio.sleep(SLEEP_FOR)
        return await fetch_recent_audit_log_entry(client, guild, target=target, action=action, retry=retry - 1)

    return None


def listens_for(*events: str) -> Callable:
    """Helper decorator which defines which events an event check is listening for.
    Parameters
    ----------
    *events: :class:`str`
        The names of the events to listen for.
    """

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        async def wrapper(client, event, *args, **kwargs):
            if event in events:
                await func(client, *args, **kwargs)

        return wrapper

    return decorator        
