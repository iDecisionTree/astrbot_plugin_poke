from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.core.message.components import ComponentType
from astrbot.api import logger
import astrbot.api.message_components as Component


@register("poke", "DecisionTree", "戳一戳", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.platform_adapter_type(filter.PlatformAdapterType.AIOCQHTTP)
    async def poke(self, event: AstrMessageEvent):

        if event.message_obj.message and event.message_obj.message[0].type is ComponentType.Poke:
            chain = [
                Component.Plain("喵")
            ]
            logger.info("触发戳一戳")
            yield event.chain_result(chain)
