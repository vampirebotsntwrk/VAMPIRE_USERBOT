import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "RAUSHAN"])

async def join(client):
    try:
        await client.join_chat("lllVAMPIRE_UPDATElll")
    except BaseException:
        pass
