# genshin-checkin
loosely followed the network capture cookie and window task scheduler from [rohk7w](https://www.reddit.com/r/Genshin_Impact/comments/rohk7w/quick_tutorial_for_building_your_own_hoyolab/)
discord embed inspired lots by [vermaysha](https://github.com/vermaysha/Hoyolab-Auto-Daily-Checkin)

docs helped with the webhook embed formating [webhook](https://discord.com/developers/docs/resources/webhook) and [embed](https://discord.com/developers/docs/resources/message#embed-object)

notes:
from looking at other repo, the main changes that breaks the claim most of the time is the signing link. in the current version of the link doesnt have the act_id attached at the end like how info and reward links have, but in the past it seems to have that extension.
act_id = "e202102251931481" the same through out versions and accounts

Discord webhook preview
![(webhook)](https://github.com/lmnhat2002vn/genshin-checkin/blob/main/webhook.png)
