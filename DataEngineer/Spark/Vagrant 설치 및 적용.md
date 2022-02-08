# Vagrant 가상환경 설치

- virtual box와 vagrant 사용



- Window

  - Virtual box 다운, 설치 
- [Windows](https://download.virtualbox.org/virtualbox/6.1.32/VirtualBox-6.1.32-149290-Win.exe) 다운 설치
- Vagrant
  - Vagrant 다운, 설치
  - [Vagrant 64bit](https://releases.hashicorp.com/vagrant/2.2.19/vagrant_2.2.19_x86_64.msi)
- Vagrant 박스 메타데이터 다운
- [spark-in-action.box](https://app.vagrantup.com/anassbo/boxes/spark-in-action-box)
- 용량이 매우커서 시간이 오래 걸림

```Vagrant
# 1. 설치가 끝나면 spark-in-action.box 파일을 C:\HashiCorp\Vagrnat 폴더 안에 넣어준다!

# 2. 폴더 안에 저장되어있는 메타 데이터 추가

vagrant box add --name manning/spark-in-action spark-in-action.box

# 3. 가상머신 사용전 초기화 진행, 명령어 실행 되면 vagrantfile이 생성되어있음을 확인 가능

vagrant init manning/spark-in-action      

# 4. vagrant 실행

vagrant up
```

- virtal box에 새로운 가상환경 생성됨 확인, 시작해서 스파크 로그인 "spark" pw "spark"
