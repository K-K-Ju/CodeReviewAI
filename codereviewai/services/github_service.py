import aiohttp

from codereviewai.config import settings


async def __fetch_repo_contents__(owner: str, repo: str, path: str = ""):
    headers = {
        "Authorization": f"Bearer {settings.github_api_key}",
        "Accept": "application/vnd.github+json"
    }
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch contents: {response.status}")
            return await response.json()

async def __traverse_repo__(owner: str, repo: str, path: str = "", file_paths=None):
    if file_paths is None:
        file_paths = []

    try:
        contents = await __fetch_repo_contents__(owner, repo, path)
        for item in contents:
            if item['type'] == 'dir':
                print(f"Directory: {item['path']}")
                await __traverse_repo__(owner, repo, item['path'], file_paths)
            elif (item['name'] == 'LICENSE' or
                  item['name'] == 'license' or
                  item['name'] == 'COPYRIGHT' or
                  item['name'] == '.gitignore' or
                  item['name'] == 'README.md'):
                continue
            elif item['type'] == 'file':
                file_paths.append((item['path'], item['download_url']))
    except Exception as e:
        print(f"Error traversing repo: {str(e)}")

    return file_paths


async def get_repo_contents(owner: str, repo: str, path: str = ""):
    file_paths = await __traverse_repo__(owner, repo, path)
    files = []

    async with aiohttp.ClientSession() as session:
        for file_path, download_link in file_paths:
            async with session.get(download_link) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch contents: {response.status}")
                content = await response.text()
                files.append(f"{file_path}\n\n{content}\n\n")

    contents_str = "".join(files)
    return contents_str


