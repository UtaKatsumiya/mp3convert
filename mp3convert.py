import os
from pydub import AudioSegment

# 1. 実行しているスクリプト(mp3convert.py)があるディレクトリを最優先で取得
base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. ffmpegのパスをOSの環境変数に追加（警告が出る前に通しておく）
ffmpeg_path = r"C:\bin\ffmpeg\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

# 3. pydubに明示的に実行ファイルの場所を教える
AudioSegment.converter = os.path.join(ffmpeg_path, "ffmpeg.exe")
AudioSegment.ffprobe = os.path.join(ffmpeg_path, "ffprobe.exe")

# --- 設定部分 ---
# スクリプトと同じ場所にある input / output フォルダを指定
input_folder = os.path.join(base_dir, "input")
output_folder = os.path.join(base_dir, "output")

# 変換対象とするファイルの拡張子
supported_extensions = ('.wav', '.m4a', '.flac', '.aac', '.wma', '.ogg')

def batch_convert_to_mp3(in_dir, out_dir):
    if not os.path.exists(in_dir):
        print(f"エラー: 入力フォルダが見つかりません: {in_dir}")
        return

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for filename in os.listdir(in_dir):
        if filename.lower().endswith(supported_extensions):
            input_path = os.path.join(in_dir, filename)
            name_without_ext = os.path.splitext(filename)[0]
            output_path = os.path.join(out_dir, f"{name_without_ext}.mp3")
            
            print(f"変換中: {filename} -> {name_without_ext}.mp3")
            
            try:
                audio = AudioSegment.from_file(input_path)
                audio.export(output_path, format="mp3", bitrate="192k")
                print("  => 成功！")
            except Exception as e:
                print(f"  => エラーが発生しました: {e}")

if __name__ == "__main__":
    print(f"作業ディレクトリ: {base_dir}")
    print("一括変換を開始します...")
    batch_convert_to_mp3(input_folder, output_folder)
    print("すべての処理が完了しました。")
