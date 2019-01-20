# Music classification

Docker Hub : https://cloud.docker.com/u/hanwjdgh/repository/docker/hanwjdgh/mlearn

## mp3 파일 tag 정보

```bash
pip install eyed3
```


## mp3 파일의 tag 정보가 깨지는 경우

- mutagen 패키지 설치

```bash
pip install mutagen
```

- mp3 파일이 있는 폴더 이동 후 ID3 태그의 인코딩 방법을 cp949에서 utf-8로 변경

```bash
find . -iname "*.mp3" -execdir mid3iconv -e cp949 {} \;
```