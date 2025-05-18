# 🤖 ML Model Management Platform

ML 모델의 라이프사이클을 관리하고 모니터링하는 통합 플랫폼입니다.

## ✨ 주요 기능

- 🔄 ML 모델 버전 관리 및 롤백
- 📊 모델 메타데이터 관리
- 📈 실시간 모니터링 및 알림
- 🔍 분산 환경에서의 로깅 및 추적
- 🔌 REST API를 통한 모델 관리
- 🐳 컨테이너화된 배포 환경

## 🛠 기술 스택

### 💻 백엔드
- 🚀 FastAPI
- 🐘 PostgreSQL
- 🔄 SQLAlchemy
- 🐍 Python 3.11

### 🏗 인프라스트럭처
- 🐳 Docker & Docker Compose
- 🌐 Nginx (리버스 프록시)
- 📊 Prometheus (메트릭 수집)
- 📈 Grafana (시각화)
- 📝 Loki (로그 수집)
- 🔍 Tempo (분산 추적)

## 🚀 시작하기

### 📋 사전 요구사항
- 🐳 Docker
- 🐳 Docker Compose
- 🐍 Python 3.11+
- 🔧 Git

### ⚙️ 설치 및 실행

1. 📥 저장소 클론
```bash
git clone <repository-url>
cd <repository-name>
```

2. ⚙️ 환경 변수 설정
```bash
cp .env.example .env
# .env 파일을 편집하여 필요한 환경 변수 설정
```

3. 🚀 서비스 실행
```bash
cd infra
docker-compose up -d
```

### 🔗 서비스 접근
- 🌐 애플리케이션: http://localhost
- 📊 Grafana 대시보드: http://localhost:3000
- 📈 Prometheus: http://localhost:9090
- 📚 API 문서: http://localhost/docs

## 🔌 API 엔드포인트

### 📦 모델 관리
- `POST /models/{model_id}`: 새 모델 등록
- `PUT /models/{model_id}/state`: 모델 상태 업데이트
- `GET /models/{model_id}/metadata`: 모델 메타데이터 조회

### 📊 모니터링
- `GET /monitor/health`: 헬스 체크
- `GET /monitor/metrics`: 메트릭 조회

## 📁 프로젝트 구조

```
.
├── 📂 app/                    # 애플리케이션 코드
│   ├── 📄 main.py            # FastAPI 애플리케이션
│   ├── 📄 models.py          # 데이터 모델
│   ├── 📄 db.py             # 데이터베이스 설정
│   └── 📄 monitor.py        # 모니터링 설정
├── 📂 infra/                 # 인프라스트럭처 설정
│   ├── 📄 docker-compose.yml # Docker Compose 설정
│   ├── 📂 nginx/            # Nginx 설정
│   ├── 📂 prometheus/       # Prometheus 설정
│   ├── 📂 grafana/          # Grafana 설정
│   ├── 📂 loki/             # Loki 설정
│   └── 📂 tempo/            # Tempo 설정
├── 📂 models/               # ML 모델 저장소
├── 📂 tests/               # 테스트 코드
├── 📄 Dockerfile           # 애플리케이션 Docker 설정
├── 📄 requirements.txt     # Python 의존성
└── 📄 README.md           # 프로젝트 문서
```

## 📊 모니터링

### 📈 메트릭
- 📊 모델 요청 수
- ⚠️ 에러율
- ⏱️ 응답 시간
- 💻 리소스 사용량

### 📝 로깅
- 📋 애플리케이션 로그
- 💾 시스템 로그
- ⚠️ 에러 로그

### 🔍 추적
- 🔎 요청 추적
- 📊 성능 분석
- 🚧 병목 현상 식별

## 🔒 보안

- 🔐 HTTPS 지원
- 🛡️ 보안 헤더 설정
- 🔑 환경 변수를 통한 민감 정보 관리
- 👥 접근 제어 및 인증

## 🤝 기여하기

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add some amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📞 연락처

👨‍💼 프로젝트 관리자 - [dhxogns920@nidsoft.com]