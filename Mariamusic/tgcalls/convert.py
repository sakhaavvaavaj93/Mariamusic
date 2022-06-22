import asyncio

from os import path


class FFmpegReturnCodeError(Exception):
    pass


async def convert(file_path: str) -> str:
    out = path.basename(file_path)
    out = out.split(".")
    out[-1] = "raw"
    out = ".".join(out)
    out = path.basename(out)
    out = path.join("raw_files", out)

    if path.isfile(out):
        return out

    try:
        proc = await asyncio.create_subprocess_shell(
            cmd=(
                "ffmpeg "
                "-y -i "
                f"{file_path} "
                "-f float32le "
                "-ac 1 "
                "-ar 44000 "
                "-acodec pcm_float32le "
                f"{out}"
            ),
            stdin=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        await proc.communicate()

        if proc.returncode != 0:
            raise FFmpegReturnCodeError("FFmpeg did not return 0")

        return out
    except:
        raise FFmpegReturnCodeError("FFmpeg did not return 0")
