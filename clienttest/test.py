import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

user_token = "user-specific-oauth-token"
user_cloud_id = "user-specific-cloud-id"

async def main():
    # Connect to streamable HTTP server with custom headers
    async with streamablehttp_client(
        "http://localhost:9000/mcp",
        headers={
            "Authorization": f"Bearer {user_token}",
            "X-Atlassian-Cloud-Id": user_cloud_id
        }
    ) as (read_stream, write_stream, _):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # Example: Get a Jira issue
            result = await session.call_tool(
                "jira_get_issue",
                {"issue_key": "PROJ-123"}
            )
            print(result)

asyncio.run(main())
