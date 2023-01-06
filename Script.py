class script(object):
    START_TXT = """<b>Hello {}

I Can Provide Movies And Series,
Just Add Me To Your Group And Enjoy.
I Work On Both Group And PM (For Owner Only).</b>"""

    HELP_TXT = """<b>Hey {}

Here Is The Help For My Commands.</b>"""

    ABOUT_TXT = """<b>✯ My Name : {}</b>

<b>✯ Creator : <a href=https://t.me/toonswood>ToonsWood</a></b>

<b>✯ Updates : <a href=https://t.me/toonswood>ToonsWood</a></b>

<b>✯ Build Status : ᴠ1.0 [Stable]</b>"""

    SOURCE_TXT ="""
<b>This Is An Private Project Of ToonsWood.In.

- Source - <a href=https://t.me/toonswood>ToonsWood</a></b>
"""
 
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter IS A Feature Were Users Can Set Automated Replies For A Particular Keyword And I Will Respond Whenever A Keyword Is Found In The Message.
<b>Note:</b>
1. This Bot Should Have Admin Privilege.
2. Only Admins Can Add Filters In A Chat.
3. Alert Buttons Have a Limit Of 64 Characters.

<u><b>Commands And Usage:</b></u>
• /filter - <code>Add A Filter In A Chat</code>
• /filters - <code>List All The Filters Of A Chat</code>
• /del - <code>Delete A Specific Filter In A Chat</code>
• /delall - <code>Delete The Whole Filters In A Chat (Chat Owner Only)</code>

~ Add The Bot As Admin On Your Group.
~ Use /connect And Connect Your Group To The Bot.
~ Use /settings On Bot's PM And Turn On/Off Auto Delete & Manual Filters On The Settings Menu."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- This Bot Supports Both URL And Alert Inline Buttons.

<b>Note:</b>
1. Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
2. This Bot Supports Buttons With Any Telegram Media Type.
3. Buttona Should Be Properly Parsed As Markdown Format.

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/toonswood)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This Is An Alert Message)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>Auto Filter</b>

<u><b>Note: File Index</b></u>
1. Make Me The Admin Of Your Channel If It's Private.
2. Make Sure That Your Channel Does Not Contains CamRips, Porn And Fake Files.
3. Forward The Last Message To Me With Quotes. I'll Add All The Files In That Channel To My DB.

<u><b>Note: Auto Filter</b></u>
1. Add The Bot As Admin On Your Group.
2. Use /connect And Connect Your Group To The Bot.
3. Use /settings On Bot's PM And Turn On/Off AutoFilter & Auto Delete On The Settings Menu.
4. Use /set_template To Set Your Custom IMDb Template."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used To Connect Bot To PM For Managing Filters. 
- It Helps To Avoid Spamming In Groups.

<b>Note:</b>
1. Only Admins Can Add A Connections.
2. Send <code>/connect</code> For Connecting Me To Your PM.

<u><b>Commands And Usage:</b></u>
• /connect  - <code>Connect A Particular Chat To Your PM</code>
• /disconnect  - <code>Disconnect From A Chat</code>
• /connections - <code>List All Your Connections</code>"""

    ADMIN_TXT = """
<code>This Module Only Works For My Admins</code>

• /logs - <code>To Get The Recent Errors</code>
• /stats - <code>To Get Status Of Files In DB.</code>
• /delete - <code>To Delete A Specific File From DB.</code>
• /deleteall - <code>To Delete All Files From DB.</code>
• /users - <code>To Get List Of My Users And IDs.</code>
• /chats - <code>To Get List Of My Chats And IDs.</code>
• /channel - <code>To Get List Of Total Connected Channels</code>
• /setskip - <code>To Skip Number Of Messages When  Indexing Files.</code>
• /leave  - <code>To Leave From A Chat.</code>
• /disable  -  <code>To Disable A Chat.</code>
• /invite - <code>To Get The Invite Link Of Any Chat Where The Bot Is Admin.</code>
• /ban_user  - <code>To Ban A User.</code>
• /unban_user  - <code>To Unban A User.</code>
• /usend - <code>To Send A Message To Particular User</code>
• /gsend - <code>To Send A Message To Particular Chat</code>
• /broadcast - <code>To Broadcast A Message To All Users</code>
• /group_broadcast - <code>To Broadcast A Message To All Connected Groups</code>
• /gfilter - <code>To Add Global Filters</code>
• /gfilters - <code>To View List Of All Global Filters<code>
• /delg - <code>To Delete A Specific Global Filter</code>
• /delallg - <code>To Delete All Global Filtercode>"""

    STATUS_TXT = """<b>📂 Files Saved:</b> <code>{}</code>
<b>👤 Users:</b> <code>{}</code>
<b>👥 Groups:</b> <code>{}</code>
<b>📉 Occupied:</b> <code>{}</code>

<b><a href=https://t.me/toonswood>Maintained By ToonsWood.In</a></b>"""

    ADMIN_STATUS_TXT = """<b>⍟────[ Bot Status ]────⍟</b>

<b>⏳ Bot Uptime:</b> <code>{}</code>

<b>☣️ CPU:</b> <code>{}%</code>

<b>☢️ RAM:</b> <code>{}%</code>

<b>📊 Files Saved:</b> <code>{}</code>

<b>👤 Users:</b> <code>{}</code>

<b>👥 Groups:</b> <code>{}</code>

<b>♻️ Total Storage:</b> <code>512 MB</code>

<b>🉐 Occupied/Used Storage:</b> <code>{}</code>

<b>🆓 Remaining/Free Storage:</b> <code>{}</code>

<b>⍟────[ @ToonsWood ]─────⍟</b>"""

    LOG_TEXT_G = """<b>#NewGroup
    
Group = {} (<code>{}</code>)

Total Members = <code>{}</code>

Added By - {}</b>
"""
    LOG_TEXT_P = """<b>#NewUser
    
Id - <code>{}</code>

Name - {}</b>
"""
    ALRT_TXT = """⚠️ Hey !
    
𝖲earch Your Own File 𝖸ᴏᴜʀ 𝖮ᴡɴ 𝖥ɪʟᴇ, 
    
Don't Click Other's Results 😬
"""

    OLD_ALRT_TXT = """⚠️ 𝖧ey ! 
    
𝖸ou Are Using One Of My Old Messages, 
    
Send The Request Again
"""

    CUDNT_FND = """<b>Sorry No File Were Found

Check Your Spelling In Google And Try Again

Read Instructions For Better Results ☟</b>
"""

    I_CUDNT = """
<b>Sorry

I Could Not Find Anything Related To That
Please Check Your Spelling 🤧</b>
"""

    I_CUD_NT = """I Couldn't Find Any Movie Related To {}.
Please Check The Spelling On Google Or IMDb...
"""

    MVE_NT_FND = """<b>Movie Not Found...
    
Reasons
𝟷) O.T.T Or DVD Not Released

𝟸) Type Name With Year

𝟹) Movie Is Not Available In The Database
Rᴇquest Here @TheToonsWood</b>
"""

    TOP_ALRT_MSG = """Checking For Movie In Database...
"""
    
    OWNER_INFO = """
<b>⍟───[ Owner Details ]───⍟
    
• Full Name : ToonsWood『🇮🇳』
• Username : @ToonsWood
• Permanent Chat Group Link : <a href='t.me/thetoonswood'>Chat Group</a></b>
"""

    KD_IMDB = """
<u><b>Commands And Usage:</b></u>

• /imdb  - <code>Get The Film Information From IMDb Source.</code>
• /search  - <code>Get The Film Information From Various Sources.</code>
"""

    KD_MISC = """
<u><b>Commands And Usage:</b></u>

• /id - <code>Get ID Of A Specified User.</code>
• /info  - <code>Get Information About A User.</code>
"""

    KD_FILSTR = """
<b>⍟ Welcome To ToonsWood File Store Module ⍟</b>

» A Module To Get Shareable Link For Any Telegram Media.

<u><b>Commands And Usage:</b></u>

• /link <code>- Replay To Any Telegram Media.<code>
• /batch <code>- To Create Link For Multiple Media.<code>

<b>Example:</b>
<code>/batch https://t.me/toonswood/1 
https://t.me/toonswood/9</code>
"""

    KD_CNL = """
<b>⍟ Channels & Groups Module ⍟</b>

<b>🎬 Complete Movie Requesting Group.
🚦 All Languages Movies & Series.
🗣️ Bot Support Group.
📢 Bot Updates Channel.</b>
"""

    FORCE_SUB = """
**⚠️ Please Follow This Rules ⚠️

In Order To Get The Movie Requested By You.

You Will Have To Join Our Official Channel First.

After That Try Accessing That Movie Then Click On The Try Again.

I'll Send You That Movie Privately.**
"""
    
    BANP_LOG_TXT = """<b>⍟ Banned User Logs ⍟</b>

<b>Admin :</b> </b> <b>{}</b>

<b>Name :</b> <b>{}</b>

<b>Reason :</b> <code>{}</code>

<b>⍟ #BannedUser ⍟</b>
"""
    UNBANP_LOG_TXT = """<b>⍟ Unbanned User Logs ⍟</b>

<b>Admin :</b> </b> <b>{}</b>

<b>Name :</b> <b>{}</b>

<b>⍟ #UnBannedUser ⍟</b>
"""
    BANG_LOG_TXT = """<b>⍟ Banned Group Logs ⍟</b>

<b>Chat ID :</b> <code>{}</code>

<b>Reason :</b> <code>{}</code>

<b>Admin :</b> </b> <b>{}</b>

<b>⍟ #BannedGroup ⍟</b>
"""
    UNBANG_LOG_TXT = """<b>⍟ Unbanned Group Logs ⍟</b>

<b>Chat ID :</b> <code>{}</code>

<b>Admin :</b> </b> <b>{}</b>

<b>⍟ #UnBannedGroup ⍟</b>
"""

    REQINFO2 = """
⚠ Information ⚠

If You Do No See The Requested Movie/Series File, Look At The Next Page
"""

    REQINFO = """
⚠ Information ⚠

After 10 Minutes This Message Will Be Automatically Deleted

If You Do No See The Requested Movie/Series File, Look At The Next Page
"""

    MINFO = """
<b>⋯⋯ Movie Request Format ⋯⋯</b>

<b>Go To Google ➠ Type Movie Name ➠ Copy Correct Name ➠ Paste Copied Movie Name In Group</b>

<b>Example : Chhota Bheem Aur Krishna</b>

<b>🚯 Don't Use ➠ ':(!,./)</b>
"""


    SINFO = """
<b>⋯⋯ Series Request Format ⋯⋯</b>

<b>Go To Google ➠ Type Movie Name ➠ Copy Correct Name ➠ Paste Copied Series Name In Group</b>

<b>Example : Chhota Bheem S01E01 or S01 E01</b>

<b>🚯 Don't Use ➠ ':(!,./)</b>
"""


    PAGEINFO = """
<b>Pages Means 10 Files In One Page</b>

<b>If you Not See Your Files On This Page Then Click On Next Page.</b>

<b>Powered By :- ToonsWood.In『🇮🇳』</b>
"""

    SPLMD = """
Movie Request Format

Example : Chhota Bheem And Krishna

Series Request Format

Example : Shiva S01E01 or S01 E01

🚯Don't Use ➠ ':(!,./)

Powered By :- ToonsWood.In『🇮🇳』
"""
    
    REQUEST_TXT = """
<u><b>📫 Request Details :</b></u>

<b>🔖 Message :</b><code>{}</code>

<b>🕵️ Requested By :</b> <b>{} [ <code>{}</code> ] </b>
"""

    REQUEST2_TXT = """
<i><b>Your Request Has Been Added!
Please Wait For Some Time.</b></i>
"""

    SGROUP_TXT = """
<b>Dear, {}

<code>{}</code> Results Are Already Available For Your Request <code>{}</code> In <a href=https://t.me/{}>Our Bot</a>.</b>
"""

    DONE_UPLOAD = """
The Request Is Completed !! Check Bot & Channel !!
"""

    REQ_REJECT = """
The Request Is Rejected Maybe Due To Same Request, Not In Format !!
"""

    REQ_NO = """
The Request Is Not Available Maybe Due To Not Released Or Not Available !!
"""

    DONE_ALREADY = """
The Request Is Already Uploaded !! Check Bot & Channel !!
""" 
    
    DONE_UPLOAD2 = """
<b>Your Request Is Successfully Uploaded Search Again..🙃</b>
"""

    REQ_REJECT2 = """
<b>Request Rejected 🚫 !!

Your Request Already MAybe In The Request List Or Your Request Is Malformatted. Kindly Request Again Or Contact Admin For Help.</b>
"""

    REQ_NO2 = """
<b>Sorry Your Request Is Not Available 😔,
Kindly Contact Admin For Help.</b>
"""

    DONE_ALREADY2 = """
<b>Request Already Uploaded ❗,
Kindly Check The Bot Before Requesting.</b>
"""

    CAP_DLT_TXT = """
<b>The Results For ☞ <code>{}</code></b>

<b>Requested By ☞ {}</b>

<b>‣ This Message Will Be Auto-Deleted After 10 Minutes.</b>
"""

    CAP_TXT = """
<b>The Results For ☞ <code>{}</code></b>

<b>Requested By ☞ {}</b>

<u><b>Hey Click On The Button Below The Files You Want And Start The Bot.</b></u>
"""
