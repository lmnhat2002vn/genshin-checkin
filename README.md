# genshin-checkin
**SAUCE:**<br>
- loosely followed the network capture cookie and window task scheduler from [rohk7w](https://www.reddit.com/r/Genshin_Impact/comments/rohk7w/quick_tutorial_for_building_your_own_hoyolab/)<br>
- discord embed inspired lots by [vermaysha](https://github.com/vermaysha/Hoyolab-Auto-Daily-Checkin)<br>
- docs helped with the webhook embed formating [webhook](https://discord.com/developers/docs/resources/webhook) and [embed](https://discord.com/developers/docs/resources/message#embed-object)<br>

**DON'T** have space in the file path cause windows scheduler will interpret that space as the end of the path and the rest will be an start arguement<br>

**notes:**<br>
<ul>
  <li>from looking at other repo, the main changes that breaks the claim most of the time is the signing link. in the current version of the link doesnt have the act_id attached at the end like how info and reward links have, but in the past it seems to have that extension and lang tags.</li>
    <ul>
      <li>old: from vermaysha</li>
        <ul>
          <li>info_url = 'https://hk4e-api-os.mihoyo.com/event/sol/info?act_id={}'.format(act_id)</li>
          <li>reward_url = 'https://hk4e-api-os.mihoyo.com/event/sol/home?act_id={}'.format(act_id)</li>
          <li>sign_url = 'https://hk4e-api-os.mihoyo.com/event/sol/sign?act_id={}'.format(act_id)</li>
        </ul>
      <li>new: mine</li>
        <ul>
          <li>info_url = "https://sg-hk4e-api.hoyolab.com/event/sol/info?lang=en-us&act_id=" + act_id</li>
          <li>reward_url = "https://sg-hk4e-api.hoyolab.com/event/sol/home?lang=en-us&act_id=" + act_id</li>
          <li>sign_url = "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us"</li>
        </ul>
    </ul>
  </li>
  <li>act_id = "e202102251931481" the same through out versions and accounts<br></li>
</ul> 

**Discord webhook preview**<br>
![(webhook)](https://github.com/lmnhat2002vn/genshin-checkin/blob/main/webhook.png)
