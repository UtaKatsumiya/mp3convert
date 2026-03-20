import os

# OSの環境変数(Path)にこの実行中だけ追加する
os.environ["PATH"] += os.pathsep + r"C:\bin\ffmpeg\bin"

from pydub import AudioSegment

# pydubにPATHを教える
AudioSegment.converter = r"C:/bin/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe = r"C:/bin/ffmpeg/bin/ffprobe.exe"

# -------------------------------------------------------------
# 確認用：これが設定したパスになっていれば準備完了
print(f"Converter Path: {AudioSegment.converter}")
print(f"FFprobe Path: {AudioSegment.ffprobe}")
# -------------------------------------------------------------

# === 設定部分 ===
# 変換元の音楽ファイルが入っているフォルダパス (r"..." のように記述します)
input_folder = r"C:\Program1\Python_code\mp3convert\input"
# 変換後のMP3を保存するフォルダパス
output_folder = r"C:\Program1\Python_code\mp3convert\output"

# 変換対象とするファイルの拡張子 (必要に応じて追加・削除してください)
supported_extensions = ('.wav', '.m4a', '.flac', '.aac', '.wma', '.ogg')
# ================

def batch_convert_to_mp3(in_dir, out_dir):
    # 出力フォルダが存在しない場合は作成する
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # フォルダ内のファイルを順番に処理
    for filename in os.listdir(in_dir):
        # 拡張子が対象のものと一致するかチェック (大文字小文字を区別しない)
        if filename.lower().endswith(supported_extensions):
            input_path = os.path.join(in_dir, filename)
            
            # 出力ファイル名の作成 (元の拡張子を削って .mp3 を付ける)
            name_without_ext = os.path.splitext(filename)[0]
            output_path = os.path.join(out_dir, f"{name_without_ext}.mp3")
            
            print(f"変換中: {filename} -> {name_without_ext}.mp3")
            
            try:
                # 音楽ファイルを読み込み
                audio = AudioSegment.from_file(input_path)
                
                # MP3として書き出し (bitrate="192k" などの音質指定も可能)
                audio.export(output_path, format="mp3", bitrate="192k")
                print("  => 成功！")
            except Exception as e:
                print(f"  => エラーが発生しました: {e}")

if __name__ == "__main__":
    print("一括変換を開始します...")
    batch_convert_to_mp3(input_folder, output_folder)
    print("すべての処理が完了しました。")