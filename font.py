from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
import random

#https://github.com/DevMrSadra
#https://github.com/DevMrSadra
#dev = https://github.com/DevMrSadra
#id telegram : devmrsadra

API_ID = 000000
API_HASH = "00000"
BOT_TOKEN = "00000000"


app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

fonts = [
    "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",  # 0
    "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",  # 1
    "??ℂ????ℍ?????ℕ?ℙℚℝ???????ℤ",  # 2
    "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ",  # 3
    "卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙",  # 4
    "ᏗᏰፈᎴᏋᎦᎶᏂᎥᏠᏦᏝᎷᏁᎧᎮᎤᏒᏕᏖᏬᏉᏇጀᎩፚ",  # 5
    "ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭Yᘔ",  # 6
    "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ",  # 7
    "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",  # 8
    "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",  # 9
    "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",  # 10
    "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",  # 11
    "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",  # 12
    "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",  # 13
    "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",  # 14
    "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𝑞ʳˢᵗᵘᵛʷˣʸᶻ",  # 15
    "ₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyz",  # 16
    "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻ",  # 17
    "ₐ𝆎𝆎𝆎ₑ𝆎𝆎𝆎ₕᵢⱼₖₗₘₙₒₚ𝆎ᵣₛₜᵤᵥ𝆎𝆎𝆎𝆎",  # 18
    "⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵",  # 19
    "ค๒ς๔єŦﻮђเןкl๓ภ๏קợгรՇยשฬאץչ",  # 20
    "αႦƈԃҽϝɠԋιʝƙʅɱɳσρϙɾʂƚυʋɯxყȥ",  # 21
    "ﾑ乃ᄃÐ乇ｷǤнﾉﾌズﾚﾶ刀ӨㄕQ尺丂ｲЦ√Щﾒﾘ乙",  # 22
    "ꋫꃃꉔ꒯ꏂꊰꍌꁝ꒐꒻ꀘ꒒ꂵꋊꄲꉣꆰꋪꇙ꓄꒤ꏝꅐꉧꌦꁴ",  # 23
    "ΛBΓDΣFGHIJKLMПӨPΩRƧƬЦ∇ЩXYZ",  # 24
    "αв¢∂єƒgнιנкℓмησρqяѕтυνωχуz",  # 25
    "ꍏꌃꉓꀸꍟꎇꁅꃅꀤꀭꀘ꒒ꂵꈤꂦꉣꆰꋪꌗ꓄ꀎᐯꅏꊼꌩꁴ",  # 26
    "【ᗅ】【ᗷ】【ᑢ】【ᗫ】【ᙍ】【ᖴ】【ᘐ】【ᕼ】【ᓰ】【ᒎ】【Ḱ】【ᒪ】【ᙢ】【ᘉ】【ᗝ】【ᕵ】【ᖳ】【ᙚ】【ᔙ】【ᖶ】【ᑘ】【ᐺ】【ᘺ】【᙭】【ᖻ】【ᗱ",  # 27
    "ꁲꁳꉔ꒯ꂅꄘꁍꃬ꒐꒻ꀘ꒒ꂵꋊꄲꉣꆺꋪꇢ꓄ꐇꏳꅏꉢꐞꁴ",  # 28
    "闩比匚刀乇下厶卄工丁长乚从𠘨口尸㔿尺丂丅凵V山乂Y乙",  # 29
    "ᥲᑲᥴᑯᥱƒɠɦɩʝƙɭოᥒ᥆ρϙɾ⳽tᥙⳳωⲭყⲍ",  # 30
    "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",  # 31
    "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",  # 32
    "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇",  # 33
    "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",  # 34
    "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",  # 35
    "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",  # 36
    "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻ",  # 37
    "ₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyz",  # 38
    "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",  # 39
    "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",  # 40
    "ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭Yᘔ",  # 41
    "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ",  # 42
    "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",  # 43
    "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",  # 44
    "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",  # 45
    "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",  # 46
    "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",  # 47
    "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",  # 48
    "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",  # 49
    "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𝑞ʳˢᵗᵘᵛʷˣʸᶻ",  # 50
    "ₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyz",  # 51
    "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻ",  # 52
    "ₐ𝆎𝆎𝆎ₑ𝆎𝆎𝆎ₕᵢⱼₖₗₘₙₒₚ𝆎ᵣₛₜᵤᵥ𝆎𝆎𝆎𝆎",  # 53
    "⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵",  # 54
    "ค๒ς๔єŦﻮђเןкl๓ภ๏קợгรՇยשฬאץչ",  # 55
    "αႦƈԃҽϝɠԋιʝƙʅɱɳσρϙɾʂƚυʋɯxყȥ",  # 56
    "ﾑ乃ᄃÐ乇ｷǤнﾉﾌズﾚﾶ刀ӨㄕQ尺丂ｲЦ√Щﾒﾘ乙",  # 57
    "ꋫꃃꉔ꒯ꏂꊰꍌꁝ꒐꒻ꀘ꒒ꂵꋊꄲꉣꆰꋪꇙ꓄꒤ꏝꅐꉧꌦꁴ",  # 58
    "ΛBΓDΣFGHIJKLMПӨPΩRƧƬЦ∇ЩXYZ",  # 59
    "αв¢∂єƒgнιנкℓмησρqяѕтυνωχуz",  # 60
    "ꍏꌃꉓꀸꍟꎇꁅꃅꀤꀭꀘ꒒ꂵꈤꂦꉣꆰꋪꌗ꓄ꀎᐯꅏꊼꌩꁴ",  # 61
    "【ᗅ】【ᗷ】【ᑢ】【ᗫ】【ᙍ】【ᖴ】【ᘐ】【ᕼ】【ᓰ】【ᒎ】【Ḱ】【ᒪ】【ᙢ】【ᘉ】【ᗝ】【ᕵ】【ᖳ】【ᙚ】【ᔙ】【ᖶ】【ᑘ】【ᐺ】【ᘺ】【᙭】【ᖻ】【ᗱ",  # 62
    "ꁲꁳꉔ꒯ꂅꄘꁍꃬ꒐꒻ꀘ꒒ꂵꋊꄲꉣꆺꋪꇢ꓄ꐇꏳꅏꉢꐞꁴ",  # 63
    "闩比匚刀乇下厶卄工丁长乚从𠘨口尸㔿尺丂丅凵V山乂Y乙",  # 64
    "ᥲᑲᥴᑯᥱƒɠɦɩʝƙɭოᥒ᥆ρϙɾ⳽tᥙⳳωⲭყⲍ",  # 65
    "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",  # 66
    "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",  # 67
    "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇",  # 68
    "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",  # 69
    "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",  # 70
    "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",  # 71
    "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻ",  # 72
    "ₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyz",  # 73
    "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",  # 74
    "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",  # 75
    "ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭Yᘔ",  # 76
    "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ",  # 77
    "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",  # 78
    "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",  # 79
    "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",  # 80
    "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",  # 81
    "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",  # 82
    "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",  # 83
    "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",  # 84
    "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𝑞ʳˢᵗᵘᵛʷˣʸᶻ",  # 85
    "ₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyz",  # 86
    "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻ",  # 87
    "ₐ𝆎𝆎𝆎ₑ𝆎𝆎𝆎ₕᵢⱼₖₗₘₙₒₚ𝆎ᵣₛₜᵤᵥ𝆎𝆎𝆎𝆎",  # 88
    "⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵",  # 89
    "ค๒ς๔єŦﻮђเןкl๓ภ๏קợгรՇยשฬאץչ",  # 90
    "αႦƈԃҽϝɠԋιʝƙʅɱɳσρϙɾʂƚυʋɯxყȥ",  # 91
    "ﾑ乃ᄃÐ乇ｷǤнﾉﾌズﾚﾶ刀ӨㄕQ尺丂ｲЦ√Щﾒﾘ乙",  # 92
    "ꋫꃃꉔ꒯ꏂꊰꍌꁝ꒐꒻ꀘ꒒ꂵꋊꄲꉣꆰꋪꇙ꓄꒤ꏝꅐꉧꌦꁴ",  # 93
    "ΛBΓDΣFGHIJKLMПӨPΩRƧƬЦ∇ЩXYZ",  # 94
    "αв¢∂єƒgнιנкℓмησρqяѕтυνωχуz",  # 95
    "ꍏꌃꉓꀸꍟꎇꁅꃅꀤꀭꀘ꒒ꂵꈤꂦꉣꆰꋪꌗ꓄ꀎᐯꅏꊼꌩꁴ",  # 96
    "【ᗅ】【ᗷ】【ᑢ】【ᗫ】【ᙍ】【ᖴ】【ᘐ】【ᕼ】【ᓰ】【ᒎ】【Ḱ】【ᒪ】【ᙢ】【ᘉ】【ᗝ】【ᕵ】【ᖳ】【ᙚ】【ᔙ】【ᖶ】【ᑘ】【ᐺ】【ᘺ】【᙭】【ᖻ】【ᗱ",  # 97
    "ꁲꁳꉔ꒯ꂅꄘꁍꃬ꒐꒻ꀘ꒒ꂵꋊꄲꉣꆺꋪꇢ꓄ꐇꏳꅏꉢꐞꁴ",  # 98
    "闩比匚刀乇下厶卄工丁长乚从𠘨口尸㔿尺丂丅凵V山乂Y乙"  # 99
]

PAGE_SIZE = 7
current_pages = {}
user_texts = {}

def get_font_buttons(text, page=0):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    buttons = []
    for i, font in enumerate(fonts[start:end]):
        transformed_text = transform_text(text, font)
        buttons.append([InlineKeyboardButton(transformed_text, callback_data=f"font_{start + i}")])

    navigation_buttons = []
    if page > 0:
        navigation_buttons.append(InlineKeyboardButton("⬅️ صفحه قبل", callback_data=f"page_{page - 1}"))
    if end < len(fonts):
        navigation_buttons.append(InlineKeyboardButton("صفحه بعد ➡️", callback_data=f"page_{page + 1}"))

    if navigation_buttons:
        buttons.append(navigation_buttons)
    return InlineKeyboardMarkup(buttons)

def transform_text(text, font_chars):
    normal_chars = "abcdefghijklmnopqrstuvwxyz"
    transformed_text = ""
    for char in text.lower():
        if char in normal_chars:
            transformed_text += font_chars[normal_chars.index(char)]
        else:
            transformed_text += char
    return transformed_text

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("سلام  خوش اومدی به ربات فونت ساز\nلطفا متن خود را ارسال کنید دقت کنید فقط انگلیسی ")

@app.on_message(filters.text & filters.private)
async def font_generator(client, message):
    user_id = message.from_user.id
    text = message.text
    if not text.isascii():
        await message.reply("لطفا فقط متن انگلیسی ارسال کنید.")
        return

    user_texts[user_id] = text  # Store the original text
    current_pages[user_id] = 0
    reply_markup = get_font_buttons(text, current_pages[user_id])
    await message.reply("یکی از فونت‌های زیر را انتخاب کنید:", reply_markup=reply_markup)

@app.on_callback_query()
async def font_selector(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data
    message = callback_query.message

    if data.startswith("font_"):
        font_index = int(data.split("_")[1])
        original_text = user_texts.get(user_id)  # Retrieve the original text
        if original_text:
            transformed_text = transform_text(original_text, fonts[font_index])
            await message.edit_text(f"متن شما:\n\n{transformed_text}",)
        else:
            await callback_query.answer("متن اصلی پیدا نشد.", show_alert=True)
    elif data.startswith("page_"):
        page = int(data.split("_")[1])
        current_pages[user_id] = page
        original_text = user_texts.get(user_id)
        if original_text:
            reply_markup = get_font_buttons(original_text, page)
            await message.edit_reply_markup(reply_markup)
            await callback_query.answer()
        else:
            await callback_query.answer("متن اصلی پیدا نشد.", show_alert=True)


app.run()