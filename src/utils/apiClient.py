from fastapi import HTTPException
import httpx
from typing import Dict, Any


async def apiClient(url: str,method="GET",data:Dict[str, Any]={}): 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://e-jagriti.gov.in/",
        "Origin": "https://e-jagriti.gov.in",
    }    
   

    async with httpx.AsyncClient() as client:
        if method=="GET":
            response = await client.get(url, headers=headers)
        elif method=="POST":
            response = await client.post(url, headers=headers,json=data)
        elif method=="PUT":
            response = await client.put(url, headers=headers,json=data)
        elif method=="DELETE":
            response = await client.delete(url, headers=headers,json=data)
        else:
            raise ValueError(f"Unsupported method: {method}")

        response.raise_for_status()
        return response.json()