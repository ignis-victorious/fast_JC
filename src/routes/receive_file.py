#
#  Import LIBRARIES
from pathlib import Path

import aiofiles
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

#  Import FILES
# #


"""Endpoint to receive and process a file."""

router: APIRouter = APIRouter()

write_path: Path = Path("/Volumes/ext/edu/py/fastapi/James_Clare_Y/fast_JC/write_dir")
filename: str = "yes.txt"


@router.post(path="/post-file")
async def post_file(file: UploadFile = File(default=...)) -> JSONResponse:
    # async def post_file(file: UploadFile = File(default=...)) -> int:
    """A simple endpoint to receive a file!"""
    async with aiofiles.open(file=write_path / filename, mode="wb") as new_file:
        # async with aiofiles.open(file="yes.txt", mode="wb") as new_file:
        contents: bytes = await file.read()
        await new_file.write(contents)
    # contents: bytes = await file.read()

    print(f"Contents: {contents}")
    return JSONResponse(content={"Fillename": file.filename, "Contents:": str(object=contents)})
    # return JSONResponse(content={"filename": file.filename})
    # return 200
