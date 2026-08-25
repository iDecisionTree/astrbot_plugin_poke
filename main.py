import random
import datetime

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
        if event.message_obj.message and event.message_obj.message[0].type is ComponentType.Poke and str(event.message_obj.message[0].id) == event.get_self_id():

            today = datetime.date.today()
            random.seed(f"{today}_{event.get_sender_id()}")

            score = random.randint(0, 100)

            if score == 100:
                desc = f"你今天的人品为：100！100！100！！！！！！"
            elif score >= 95:
                desc = f"你今天的人品为：{score}！差点就到100了呢……"
            elif score >= 90:
                desc = f"你今天的人品为：{score}！好评如潮喵！"
            elif score >= 70:
                desc = f"你今天的人品为：{score}！今天运气不错呢喵！"
            elif score >= 40:
                desc = f"你今天的人品为：{score}，还行啦，还行啦。"
            elif score >= 20:
                desc = f"你今天的人品为：{score}！呜……"
            elif score >= 10:
                desc = f"你今天的人品为：{score}？！不会吧……"
            else:
                desc = f"你今天的人品为：{score}……（是百分制哦）"

            chain = [Component.Plain(desc)]
            yield event.chain_result(chain)
