# AWS Diagram Design Skill(aws-diagram-design)

**한국어** | [English](README.en.md) · [갤러리](https://masangbeom.github.io/aws-diagram-design/)

**말로 설명하면, AWS 다이어그램을 작성합니다.**

draw.io 등을 사용하여 다양한 아키텍처 및 다이어그램을 작성하는 대신, Claude Code나 Kiro에게 이렇게 말해보세요.

> "ALB 뒤에 Fargate 서비스 두고, RDS Multi-AZ랑 ElastiCache 붙는 VPC 3-티어 구성도 그려줘"

[공식 AWS Architecture Icons](https://aws.amazon.com/ko/architecture/icons/)와 Amazon Ember 타이포그래피, VPC/서브넷/계정 컨테이너 규약까지 적용된 다이어그램이 자체 완결형 HTML로 생성되고, 필요하면 SVG/PNG로 바로 내보낼 수 있습니다. 제안서, 위키, 발표 자료, 아키텍처 리뷰에 그대로 쓸 수 있는 품질을 목표로 합니다.

## 이런 걸 그려줍니다

- **아키텍처 구성도**: 서버리스, VPC 네트워크, 멀티 계정/멀티 리전, 하이브리드(Direct Connect/VPN)까지. VPC/서브넷/Region/계정 경계는 공식 그룹 컨테이너 색상/배지 규약을 따릅니다.
- **운영/설계 문서에 쓰는 나머지 전부**: 플로차트, 시퀀스, 상태 머신, ER·DB 스키마, 타임라인, 스윔레인, 간트, 조직도, 레이어 스택, 데이터 플로, 배포·의존성 그래프, 아키텍처 Before/After 비교(delta), 워터폴·생키·트리맵·히트맵 차트, 서비스 블루프린트, 워들리 맵 등 총 45개 시각 타입.
- **기존 다이어그램 재작도**: 갖고 있는 draw.io(.drawio)나 Mermaid(.mmd) 파일을 읽어 내용은 유지한 채 지정한 크기와 상세도(문서용/슬라이드용/요약본)로 다시 그립니다.

AWS 서비스를 명명하는 노드에는 다이어그램 타입에 관계없이 공식 아이콘이 들어가고, 강조는 smile orange 포컬 1–2개로 절제하는 에디토리얼 디자인 시스템([cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) 2.6 기반)이 적용됩니다.

## AWS 엔지니어가 봐도 맞는 다이어그램

모양만 AWS처럼 보이는 게 아니라 AWS 엔지니어가 읽어도 틀린 데가 없도록, 타입마다 **On AWS** 규칙을 두고 그리는 단계에서 바로 적용합니다.

- **배치가 곧 주장입니다**: S3, DynamoDB, SQS 같은 리전 서비스는 VPC 밖에 두고 VPC 엔드포인트로 연결합니다. CloudFront, Route 53, IAM 같은 글로벌 서비스는 Region 밖에 둡니다. 인터넷용 ALB와 NAT 게이트웨이는 퍼블릭 서브넷에 둡니다.
- **Multi-AZ는 그림으로**: Multi-AZ 리소스는 AZ 열 전체에 걸쳐 그립니다. 하나의 AZ에 넣어 두고 라벨로만 Multi-AZ라고 쓰지 않습니다.
- **공식 서비스 이름**: 처음 언급할 때는 `AWS Lambda`, `Amazon EC2`처럼 접두어까지 정확히 쓰고, 이후에는 짧게 씁니다. Amazon SageMaker AI, Amazon Data Firehose 같은 최신 명칭을 씁니다.
- **동작도 실제대로**: 동기/비동기 호출(`202`, `MessageId`), Step Functions 상태(`ABORTED` 등), CDK → CloudFormation 배포 같은 실제 동작을 따릅니다.
- **대비 기준**: 라이트 스킨에서 smile orange는 선·마커·채움에만 쓰고 작은 텍스트에는 쓰지 않습니다(WCAG 대비 기준).

아이콘은 번들된 `scripts/aws_icon.py`로 찾아서 삽입하고(`aws_icon.py find dynamodb`), 결과물은 `scripts/self_check.py`로 접근성·단일 파일 안전성·문서 완결성을 스스로 점검합니다.

## 미리보기

아래는 모두 이 스킬로 생성한 결과물입니다. 원본 HTML·SVG·PNG는 [docs/samples/](docs/samples/)에 있습니다.

### Serverless Web Application

가장 흔한 시작점. CloudFront가 S3 정적 자산과 API Gateway → Lambda → DynamoDB 동적 경로를 분기합니다. ([HTML](docs/samples/serverless-web-app.html) · [SVG](docs/samples/serverless-web-app.svg))

![Serverless Web Application 아키텍처 다이어그램](docs/samples/serverless-web-app.png)

### VPC Three-Tier Web Service

us-east-1의 가용 영역 두 개(1a/1b)마다 퍼블릭·앱·데이터 서브넷을 두는 정석 구조입니다. 두 AZ에 걸친 인터넷용 ALB가 각 AZ의 ECS on Fargate 태스크로 트래픽을 보내고, RDS for PostgreSQL Multi-AZ(primary 1a · standby 1b)와 ElastiCache(Valkey) 복제 그룹이 두 데이터 서브넷에 걸쳐 그려집니다. AWS Cloud ⊃ Region ⊃ VPC ⊃ AZ ⊃ 서브넷 경계와 배지는 공식 규약을 그대로 따릅니다. ([HTML](docs/samples/vpc-three-tier.html) · [SVG](docs/samples/vpc-three-tier.svg))

![VPC Three-Tier Web Service 아키텍처 다이어그램](docs/samples/vpc-three-tier.png)

### Event-Driven Data Pipeline

Kinesis Data Streams → AWS Lambda → Amazon S3 데이터 레이크 스트리밍 수집과, Glue Data Catalog를 거쳐 Amazon Athena가 S3를 직접 스캔하는 분석 경로. 교차하는 커넥터는 bridge/hop으로 처리됩니다. ([HTML](docs/samples/event-driven-pipeline.html) · [SVG](docs/samples/event-driven-pipeline.svg))

![Event-Driven Data Pipeline 아키텍처 다이어그램](docs/samples/event-driven-pipeline.png)

### Multi-Region Network Backbone

멀티 계정/멀티 리전 네트워크의 전형적인 모양. 리전별 Network account의 AWS Transit Gateway가 AWS Cloud WAN 코어로 피어링되고, 온프레미스는 AWS Direct Connect(BGP) + Site-to-Site VPN 백업으로 연결됩니다. ([HTML](docs/samples/multi-region-network.html) · [SVG](docs/samples/multi-region-network.svg))

![Multi-Region Network Backbone 아키텍처 다이어그램](docs/samples/multi-region-network.png)

### AWS Data Pipeline Flow

"누가 어느 단계에서 무엇을 하는가"를 보여주는 역할 스코프 데이터 플로. Data Admin이 Lake Formation 카탈로그 거버넌스와 IAM 접근 권한을 점선 트리거로 내려주고, 그 아래에서 Firehose/DMS 수집 → S3 레이크 → Glue ETL → Redshift DW(포컬 핸드오프) → Quick Sight 대시보드로 이어집니다. 각 노드의 공식 서비스 아이콘과 하단 칩이 페이로드 타입 변환(스트림→데이터셋→테이블→리포트)을 추적합니다. ([HTML](docs/samples/data-pipeline-flow.html) · [SVG](docs/samples/data-pipeline-flow.svg))

![AWS Data Pipeline Flow 다이어그램](docs/samples/data-pipeline-flow.png)

> 위 이미지는 Amazon Ember로 렌더링한 PNG입니다. SVG는 단독 파일로 내보낸 것이지만 GitHub 이미지 뷰어가 외부 폰트를 막아 시스템 폰트로 보이므로, 원래 모습 그대로 보려면 HTML을 브라우저에서 여세요.

### 전체 갤러리

45개 타입 전부의 예제 201개(라이트 / 다크 / 에디토리얼 풀 페이지, 일부 애니메이션)가 모두 AWS 시나리오로 들어 있습니다. 예를 들면 EC2 → Fargate 마이그레이션 before/after, Cognito 토큰 갱신 시퀀스, Step Functions 배치 작업 상태, S3 데이터 레이크, AWS 비용 워터폴·트리맵, Organizations OU 트리 같은 것들입니다. 스킬은 이 예제들을 타입별 기준 렌더로 참고합니다.

**온라인 갤러리: [masangbeom.github.io/aws-diagram-design/](https://masangbeom.github.io/aws-diagram-design/)** (GitHub Pages, `main`에 머지할 때마다 자동 배포)

로컬에서 보려면:

```bash
python3 -m http.server 8765 --directory skills/aws-diagram-design/assets
# → http://127.0.0.1:8765/index.html
```

상단 목록에서 타입과 변형을 고르고, 오른쪽 위 탭으로 라이트 / 다크 / 풀 페이지를 바꿔 볼 수 있습니다. `aws-icons.html`은 번들된 공식 아이콘 812종을 보여주는 갤러리입니다.

## 시작하기

### Claude Code

```
/plugin marketplace add masangbeom/aws-diagram-design
```
```
/plugin install aws-diagram-design@aws-diagram-design
```
```
/reload-plugins
```

로컬에 클론해 뒀다면 경로로 등록해도 됩니다: `/plugin marketplace add /path/to/aws-diagram-design`.

### Kiro (IDE / CLI)

```bash
./install.sh kiro            # ~/.kiro/skills/ 에 복사 (--workspace: 프로젝트 로컬, --link: 심링크)
```

Kiro는 Anthropic 형식 Agent Skills를 그대로 읽으므로 별도 변환이 없습니다. Power로 등록하는 방법은 [docs/guide-kiro.md](docs/guide-kiro.md) 참고.

### 폰트 (선택)

```bash
./install.sh fonts           # 번들된 Amazon Ember TTF를 OS 폰트 디렉터리에 설치
```

Amazon Ember는 [Amazon 공식 배포본](https://developer.amazon.com/en-US/alexa/branding/echo-guidelines/identity-guidelines/typography)을 스킬에 번들해 두었습니다(`skills/aws-diagram-design/assets/fonts/`). 생성되는 다이어그램은 로컬 설치본 → 번들 woff2 → Helvetica 순으로 폰트를 찾으므로, 설치하지 않아도 동작에는 문제가 없습니다.

## 이렇게 써보세요

평소 쓰는 말로 요청하면 됩니다. 한국어 트리거(구성도, 아키텍처 다이어그램, 흐름도, 시퀀스 다이어그램 등)를 인식합니다.

```
"이 프로젝트 아키텍처 구성도 그려줘. EKS에 ArgoCD 배포, RDS는 Multi-AZ"
"Transit Gateway 허브-스포크 네트워크 구성도, 계정 3개짜리로"
"AWS 주문 처리 시퀀스 다이어그램 그려줘 — API Gateway, Lambda, SQS, DynamoDB"
"이 온보딩 프로세스를 스윔레인으로 정리해줘"
```

기존 파일 재작도와 내보내기는 슬래시 커맨드로:

```
/aws-diagram-design:import-drawio legacy-arch.drawio     # draw.io 파일을 다시 그리기
/aws-diagram-design:import-mermaid pipeline.mmd          # Mermaid 파일을 다시 그리기
/aws-diagram-design:export-diagram my-diagram.html       # 생성된 HTML을 SVG/PNG로 내보내기
```

재작도 시 크기(문서 인라인/와이드/슬라이드 16:9/A3 인쇄/소셜 카드), 상세도(faithful/balanced/simplified), 독자(엔지니어/혼합/경영진)를 지정할 수 있고, 병합되거나 생략된 요소는 fidelity ledger로 보고됩니다.

내보내기는 번들 스크립트(`export_svg.py`, `export_png.py`)로 실행됩니다. SVG는 페이지 CSS와 Amazon Ember `@font-face`를 그대로 담은 단독 파일로 나오고, PowerPoint에서 깨지지 않도록 색상을 정규화합니다. PNG는 Playwright가 설치된 환경에서만 만들 수 있습니다.

## AWS 공식 리소스를 그대로 씁니다

| 리소스 | 내용 |
|---|---|
| [AWS Architecture Icons](https://aws.amazon.com/ko/architecture/icons/) | 공식 아이콘 패키지(릴리스 07312026) 812종 번들: 서비스 305, 리소스 466, 그룹 15, 카테고리 26. 변형/재채색 없이 원본 그대로 사용하며, 아키텍처 외 모든 다이어그램 타입에도 적용됩니다. 갤러리: `assets/aws-icons.html` |
| 그룹 컨테이너 규약 | AWS Cloud, 계정, Region, VPC, 퍼블릭/프라이빗 서브넷, 보안 그룹 등의 공식 경계 색상/배지/점선 규칙 |
| [Amazon Ember](https://developer.amazon.com/en-US/alexa/branding/echo-guidelines/identity-guidelines/typography) | 공식 배포 폰트 번들(woff2 + TTF). squid ink `#232F3E` + smile orange `#EC7211`/`#FF9900` 팔레트와 함께 AWS 브랜드 스킨을 구성 |

## 저장소 구조

```
aws-diagram-design/
├── .claude-plugin/                 # Claude Code 플러그인 매니페스트 + 마켓플레이스 카탈로그
├── .github/workflows/pages.yml     # 갤러리를 GitHub Pages로 배포
├── plugin.json                     # Agent Plugins 매니페스트 (Kiro Power용)
├── commands/                       # 슬래시 커맨드 3종 (import-drawio / import-mermaid / export-diagram)
├── skills/aws-diagram-design/      # 정본 스킬 (모든 환경 공용)
│   ├── SKILL.md                    #   설계 시스템 + 45개 타입 라우팅
│   ├── references/                 #   스펙 58개 (style-guide, type-* 45종과 On AWS 규칙, primitive-aws-icons 등)
│   ├── assets/                     #   템플릿, AWS 예제 201개 + 갤러리(index.html), aws-icons/ 812 SVG, fonts/ Amazon Ember
│   └── scripts/                    #   자체 검증(self_check, verify-geometry), drawio/mermaid 추출기, SVG/PNG 내보내기(export_svg, export_png), AWS 아이콘 삽입(aws_icon)
├── scripts/                        # 저장소 수준 검증기 20종(geometry, motion, 차트별) + 테스트 9종 + fixtures
├── docs/                           # 환경별 한글 가이드 + samples/ 예제 다이어그램
└── install.sh                      # claude-code · kiro · fonts 설치
```

## 라이선스

MIT. 서드파티 고지는 [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) 참고. AWS Architecture Icons는 [AWS 아이콘 이용 약관](https://aws.amazon.com/ko/architecture/icons/)을 따르며 변형/재채색이 금지되고, Amazon Ember는 동봉된 라이선스 가이드라인을 따릅니다.
