from pathlib import Path
import os
import math


def format_duration(milliseconds: int) -> str:
    total_seconds = round(milliseconds / 1000)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def configure_ffmpeg():
    """
    Solicita o caminho do ffmpeg.exe e adiciona temporariamente
    sua pasta ao PATH desta execução.
    """
    ffmpeg_path = input("Informe o caminho completo do executável ffmpeg: ").strip().strip('"')
    ffmpeg_file = Path(ffmpeg_path)

    if not ffmpeg_file.exists():
        print(f"Erro: ffmpeg não encontrado em: {ffmpeg_file}")
        return None

    if ffmpeg_file.name.lower() != "ffmpeg.exe":
        print("Aviso: o arquivo informado não parece ser o ffmpeg.exe")

    ffmpeg_dir = ffmpeg_file.parent

    # adiciona a pasta do ffmpeg ao PATH apenas nesta execução
    os.environ["PATH"] = str(ffmpeg_dir) + os.pathsep + os.environ.get("PATH", "")

    ffprobe_file = ffmpeg_dir / "ffprobe.exe"
    if not ffprobe_file.exists():
        print(f"Erro: ffprobe.exe não encontrado na mesma pasta do ffmpeg: {ffprobe_file}")
        return None

    return ffmpeg_file, ffprobe_file


def split_mp3(input_file: str, chunk_minutes: int = 15) -> None:
    """
    Divide um arquivo MP3 em partes de chunk_minutes minutos.
    """
    from pydub import AudioSegment

    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Erro: arquivo não encontrado: {input_path}")
        return

    if input_path.suffix.lower() != ".mp3":
        print("Erro: o arquivo informado não é um arquivo .mp3")
        return

    try:
        audio = AudioSegment.from_mp3(str(input_path))
    except Exception as e:
        print("Erro ao abrir o arquivo MP3.")
        print("Verifique se ffmpeg.exe e ffprobe.exe estão na mesma pasta.")
        print(f"Detalhes: {e}")
        return

    total_duration_ms = len(audio)
    chunk_length_ms = chunk_minutes * 60 * 1000
    total_parts = math.ceil(total_duration_ms / chunk_length_ms)

    print("\n" + "=" * 60)
    print(f"Arquivo original: {input_path.name}")
    print(f"Duração total:    {format_duration(total_duration_ms)}")
    print(f"Tamanho do trecho: {chunk_minutes} minutos")
    print(f"Total de partes:   {total_parts}")
    print("=" * 60)

    base_name = input_path.stem
    output_dir = input_path.parent

    for i in range(total_parts):
        start_ms = i * chunk_length_ms
        end_ms = min((i + 1) * chunk_length_ms, total_duration_ms)

        chunk = audio[start_ms:end_ms]

        output_name = f"{base_name}_part{i + 1}.mp3"
        output_path = output_dir / output_name

        try:
            chunk.export(str(output_path), format="mp3")
            print(f"{output_name}  |  duração: {format_duration(len(chunk))}")
        except Exception as e:
            print(f"Erro ao salvar {output_name}: {e}")

    print("=" * 60)
    print("Processo concluído.")


def main():
    print("=== Divisor de arquivos MP3 ===\n")

    ffmpeg_info = configure_ffmpeg()
    if ffmpeg_info is None:
        return

    input_file = input("\nInforme o caminho completo do arquivo .mp3: ").strip().strip('"')
    split_mp3(input_file, chunk_minutes=15)


if __name__ == "__main__":
    main()