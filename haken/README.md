#anacondaでバージョン切り替えする方法
##仮想環境の作成-pythonでバージョンを切り替える際などに利用する-
conda create --name myenv python=3.7
conda create --name python_env3.9 python=3.9

##作成した仮想環境への切り替え
conda activate myenv
##エクセルの仮想環境へ切り替え
conda activate python_env3.9

##別のバージョンのPythonをインストール:
conda install python=3.7

##インストールされたPythonのバージョンを切り替える:
conda activate base  # 仮にデフォルトの環境が"base"としています
conda activate python=3.7  # 切り替えたいバージョンに合わせて変更


##仮想環境一覧を表示する
conda env list


#ブヘラーをcsvに抽出する。
##スプレッドシートでoutput.csvを開く
##そのデータをエクセルに張り付け





サイズ、素材の場所を変える
