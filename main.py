import asyncio
from dotenv import load_dotenv

from models.model_client import get_model_client
from teams.document_intelligence import getDocumentIntelligenceTeam


load_dotenv()


async def main():
    gemini_model_client = get_model_client()

    team = getDocumentIntelligenceTeam(gemini_model_client)

    task = '''
    Process the csv data for PPE log analysis
    timestamp,worker_id,ppe_item,status,severity,location
    8/30/2025 15:52,W107,Face_Shield,Compliant,None,Yard
    8/28/2025 21:00,W101,Safety_Jacket,Non-Compliant,High,Yard
    8/28/2025 2:48,W104,Gloves,Compliant,None,Yard
    8/25/2025 15:18,W102,Mask,Compliant,None,Maintenance
    8/29/2025 0:28,W110,Helmet,Compliant,None,Meltshop
    8/30/2025 2:53,W104,Safety_Jacket,Compliant,None,Maintenance
    8/29/2025 14:30,W103,Helmet,Compliant,None,Meltshop
    8/27/2025 20:24,W103,Goggles,Compliant,None,Rolling
    8/25/2025 20:44,W110,Goggles,Non-Compliant,Low,Meltshop
    9/1/2025 2:42,W101,Gloves,Compliant,None,Meltshop
    8/30/2025 23:46,W100,Mask,Non-Compliant,Low,Meltshop
    8/30/2025 19:46,W100,Helmet,Compliant,None,Yard
    8/31/2025 18:21,W105,Helmet,Compliant,None,Yard
    9/1/2025 7:02,W107,Helmet,Non-Compliant,Medium,Meltshop
    8/29/2025 23:06,W110,Gloves,Non-Compliant,Low,Meltshop
    8/26/2025 11:28,W106,Mask,Non-Compliant,Medium,Meltshop
    8/26/2025 16:12,W100,Safety_Jacket,Compliant,None,Maintenance
    8/28/2025 3:29,W110,Safety_Jacket,Compliant,None,Yard
    8/31/2025 3:32,W110,Safety_Jacket,Non-Compliant,High,Yard
    8/29/2025 11:05,W107,Goggles,Non-Compliant,Low,Meltshop

    '''

    try:
        async for message in team.run_stream(task=task):
            print(message.source)
            print(message.content)

    except Exception as e:
        print(e)

if (__name__ == "__main__"):
    asyncio.run(main())
