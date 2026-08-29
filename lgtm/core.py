import click

@click.command()
@click.option('--message', '-m', default='LGTM',
              show_default=True, help='画像に載せる文字列')
@click.argument('keyword')


def cli():
    """LGTM画像生成ツール"""
    lgtm(keyword, message)
    click.echo('lgtm') # 動作確認用


def lgtm():
    # ここにロジックを追加していきます
    pass