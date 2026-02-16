<div align="center">

# 🤖 ML Model Management Platform

**ML 모델의 라이프사이클을 관리하고 모니터링하는 통합 플랫폼**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MariaDB](https://img.shields.io/badge/MariaDB-11-003545?style=flat-square&logo=mariadb&logoColor=white)](https://mariadb.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Nginx-Proxy-009639?style=flat-square&logo=nginx&logoColor=white)](https://nginx.org/)
[![Prometheus](https://img.shields.io/badge/Prometheus-Metrics-E6522C?style=flat-square&logo=prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800?style=flat-square&logo=grafana&logoColor=white)](https://grafana.com/)

[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/your-username)

</div>

---

## ✨ 주요 기능

| | 기능 |
|---|------|
| 🔄 | ML 모델 버전 관리 및 롤백 |
| 📊 | 모델 메타데이터 관리 |
| 📈 | 실시간 모니터링 및 알림 |
| 🔍 | 분산 환경 로깅 및 추적 |
| 🔌 | REST API를 통한 모델 관리 |
| 🐳 | 컨테이너화된 배포 환경 |

---

## 🛠 기술 스택

<table>
<tr>
<td width="50%">

#### 💻 백엔드

| 기술 | 설명 |
|------|------|
| ![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white) | 런타임 |
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | API 프레임워크 |
| ![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=mariadb&logoColor=white) | 데이터베이스 |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat-square) | ORM |

</td>
<td width="50%">

#### 🏗 인프라

| 기술 | 역할 |
|------|------|
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) | 컨테이너 |
| ![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white) | 리버스 프록시 |
| ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) | 메트릭 수집 |
| ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white) | 시각화 |
| ![Loki](https://img.shields.io/badge/Loki-2.8-FF6B6B?style=flat-square) | 로그 수집 |
| ![Tempo](https://img.shields.io/badge/Tempo-1.6-FF6B6B?style=flat-square) | 분산 추적 |

</td>
</tr>
</table>

---

## 🚀 시작하기

### 📋 사전 요구사항

- **Docker** & **Docker Compose**
- **Python 3.11+** (로컬 실행 시)
- **Git**

---

### ⚙️ Docker로 실행 (권장)

```bash
git clone <repository-url>
cd <repository-name>

# 환경 변수 (선택)
cp .env.example .env

# 전체 스택 실행
cd infra && docker-compose up -d
```

#### 🔗 서비스 접근

| 서비스 | URL |
|--------|-----|
| 🌐 애플리케이션 | http://localhost |
| 📚 API 문서 | http://localhost/docs |
| 📊 Grafana | http://localhost:3000 |
| 📈 Prometheus | http://localhost:9090 |

---

### 💻 로컬에서 실행 (Docker 없이)

FastAPI 앱만 실행됩니다. Nginx·Grafana·Prometheus는 포함되지 않습니다.

**필요 조건**

- Python 3.11+
- **MariaDB**가 `localhost:3306`에서 실행 중
- DB `modeldb` 및 사용자 `modeluser` / 비밀번호 `modeldb` (또는 `DATABASE_URL`로 지정)

```bash
# 프로젝트 루트에서
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# DB 연결 (기본값)
export DATABASE_URL="mysql+pymysql://modeluser:modeldb@localhost:3306/modeldb"

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

| 항목 | 로컬 실행 시 |
|------|----------------|
| 앱 | http://localhost:8000 |
| API 문서 | http://localhost:8000/docs |

> ⚠️ MariaDB가 꺼져 있으면 앱 기동 시 DB 연결 오류로 실패합니다.

---

## 🔌 API 엔드포인트

#### 📦 모델 관리

| Method | Endpoint | 설명 |
|--------|----------|------|
| `POST` | `/models/{model_id}` | 새 모델 등록 |
| `PUT` | `/models/{model_id}/state` | 모델 상태 업데이트 |
| `GET` | `/models/{model_id}/metadata` | 모델 메타데이터 조회 |

#### 📊 모니터링

| Method | Endpoint | 설명 |
|--------|----------|------|
| `GET` | `/monitor/health` | 헬스 체크 |
| `GET` | `/monitor/metrics` | 메트릭 조회 |

---

## 📁 프로젝트 구조

```
├── app/                    # 애플리케이션
│   ├── main.py             # FastAPI 진입점
│   ├── models.py           # 도메인 모델
│   ├── db.py               # DB 설정 (MariaDB)
│   ├── model_controller.py
│   ├── version_controller.py
│   └── monitor.py
├── infra/                  # 인프라
│   ├── docker-compose.yml
│   ├── nginx/
│   ├── prometheus/
│   ├── grafana/
│   ├── loki/
│   └── tempo/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 📊 모니터링

| 영역 | 내용 |
|------|------|
| **메트릭** | 모델 요청 수, 에러율, 응답 시간, 리소스 사용량 |
| **로깅** | 애플리케이션 / 시스템 / 에러 로그 |
| **추적** | 요청 추적, 성능 분석, 병목 식별 |

---

## 🔒 보안

- HTTPS 지원
- 보안 헤더 설정
- 환경 변수 기반 민감 정보 관리
- 접근 제어 및 인증

---

## 🤝 기여하기

1. 저장소 Fork
2. 기능 브랜치 생성 (`git checkout -b feature/amazing-feature`)
3. 변경 사항 커밋 (`git commit -m 'Add some amazing feature'`)
4. 브랜치 푸시 (`git push origin feature/amazing-feature`)
5. Pull Request 생성

---

## 📄 라이선스

이 프로젝트는 **MIT** 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE)를 참조하세요.

---

## ☕ 후원하기

이 프로젝트가 도움이 되었다면 커피 한 잔으로 응원해 주세요.

[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/rosieoh)

---

## 📞 연락처

**프로젝트 관리자** — [dhxogns920@gmail.com](mailto:dhxogns920@gmail.com)
