def main():
    import os
    import git
    import subprocess

    path = ''#Pushしたいローカルリポジトリへのパス
    command = ['procon-gardener', 'archive']
    command_check_str = 'Archiving 0 code...'

    # コマンドの実行と結果の取得
    result = subprocess.run(command, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT).stdout

    # 結果をデコードする
    decoded_result = result.decode()

    # 取得するコードがあればPush、ないならば終了
    if command_check_str in decoded_result:
        exit()

    # Pushするローカルリポジトリへ移動
    os.chdir(path)
    repo = git.Repo()

    # リモートリポジトリから最新を取り込むためPullする
    o = repo.remotes.origin
    o.pull()

    # Pushする
    origin = repo.remote(name='origin')
    origin.push()


if __name__ == '__main__':
    main()
