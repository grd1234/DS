from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

#initialize FastMCP server
mcp = FastMCP("weather")

#constants
#API_KEY = "YOUR_API_KEY"

NWS_API_BASE_URL = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """
    Make a request to the NWS API with proper error handling
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers,timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            return None
        
    
def format_alert(feature:dict) -> str:
    """
    Format a weather alert as a string
    """
    props = feature["properties"]
    return f"""
        Event: {props.get("event", "Unknown Event")}
        Area: {props.get("areaDesc", "N/A")}
        Serverity: {props.get("severity", "N/A")}
        Description: {props.get("description", "No additional information")}
        Instructions: {props.get("instruction", "No additional information")}
        """


@mcp.tool()
async def get_weather_alerts(state: str):
    """
    Get current weather alerts from the NWS API for a specific US state
    Args:
        state (str): The US state to get weather alerts for
        Example: "CA"
        state: two letter US state code (e.g. CA, TX, NY, etc.)
    Returns:
        str: A string containing all active weather alerts for the given state
    """
   
    url = f"{NWS_API_BASE_URL}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "No data or weather alerts found"
    
    if not data["features"]:
        return "No active weather alerts found "
    
    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n".join(alerts)

@mcp.tool()
async def fetch_city_weather(city: str, state: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:
        url = f"{NWS_API_BASE_URL}/alerts/active/area/{state}/{city}"
        data = await make_nws_request(url)

        if not data or "features" not in data:
            return "No data or weather alerts found"
    
        if not data["features"]:
            return "No active weather alerts found "
        
        alerts = [format_alert(feature) for feature in data["features"]]
        return "\n".join(alerts)

@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    return f"Profile data for user {user_id}"

@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"