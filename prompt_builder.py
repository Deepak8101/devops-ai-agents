def build_prompt(system_info):

    prompt = f"""
You are a Senior Linux System Administrator.

Analyze this Linux system.

Hostname:
{system_info["hostname"]}

Disk:
{system_info["disk"]}

Memory:
{system_info["memory"]}

Uptime:
{system_info["uptime"]}

Return ONLY valid JSON.

Example format:

{{
    "overall_health":"",
    "disk": {{
        "status":"",
        "reason":""
    }},
    "memory": {{
        "status":"",
        "reason":""
    }},
    "performance": {{
        "status":"",
        "reason":""
    }},
    "recommendations":[]
}}

Do not return markdown.

Do not use ```json.
"""

    return prompt
