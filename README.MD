# Como Contribuir com Image2WorldLib

Este guia explica como configurar o ambiente de desenvolvimento e publicar uma nova versão do pacote Image2WorldLib no PyPI.

## Pré-requisitos

- Python 3.8 ou superior
- Git instalado
- Conta no PyPI (para publicação)
- Token de API do PyPI

## Configuração do Ambiente de Desenvolvimento

### 1. Criar Diretório do Projeto

```bash
mkdir Image2WorldLib
cd Image2WorldLib
```

### 2. Configurar pyproject.toml

Crie o arquivo `pyproject.toml` na raiz do projeto com o seguinte conteúdo:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "image2world"
version = "0.2.0"
description = "A package to compute tridimensional bounding boxes from bidimensional bounding boxes and depth data"
authors = [
    { name = "João Francisco de Souza Santos Lemos" }
]
maintainers = [
    { name = "João Francisco de Souza Santos Lemos" }
]
readme = "README.md"
license = { text = "MIT License" }
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[tool.setuptools.packages.find]
where = ["Image2WorldLib"]
```

**⚠️ Importante:** Altere a versão para a desejada antes de publicar!

### 3. Clonar o Repositório

```bash
git clone https://github.com/Jfsslemos/Image2WorldLib
```

## Processo de Publicação

### 1. Instalar Dependências de Build

```bash
pip install --upgrade build twine
```

### 2. Construir o Pacote

```bash
python -m build
```

Este comando criará os arquivos de distribuição na pasta `dist/`.

### 3. Publicar no PyPI

```bash
twine upload dist/*
```

Quando solicitado, insira:
- **Username:** `__token__`
- **Password:** Sua chave de API do PyPI

## Estrutura do Projeto

```
Image2WorldLib/
├── Image2WorldLib/          # Código fonte do pacote
│   ├── __init__.py
│   └── ...                  # Módulos do pacote
├── pyproject.toml           # Configuração do projeto
├── README.md               # Documentação
├── LICENSE                 # Arquivo de licença
└── dist/                   # Arquivos de distribuição (gerados)
```

## Dicas Importantes

### Versionamento
- Siga o padrão [Semantic Versioning](https://semver.org/)
- Formato: `MAJOR.MINOR.PATCH`
- Exemplo: `0.2.1` → `0.2.2` (patch), `0.2.2` → `0.3.0` (minor)

### Antes de Publicar
1. ✅ Atualize a versão no `pyproject.toml`
2. ✅ Teste o código localmente
3. ✅ Atualize a documentação se necessário
4. ✅ Verifique se todos os arquivos estão commitados

### Comandos Úteis

```bash
# Limpar arquivos de build anteriores
rm -rf dist/ build/ *.egg-info/

# Verificar se o pacote pode ser instalado localmente
pip install -e .

# Testar upload no TestPyPI primeiro (recomendado)
twine upload --repository testpypi dist/*
```

## Configuração da API Key do PyPI

1. Acesse [PyPI Account Settings](https://pypi.org/manage/account/)
2. Vá em "API tokens"
3. Crie um novo token com escopo adequado
4. Use o token como senha no comando `twine upload`

## Solução de Problemas

### Erro: "File already exists"
- A versão já foi publicada
- Incremente a versão no `pyproject.toml`

### Erro: "Invalid credentials"
- Verifique se está usando `__token__` como username
- Confirme se a API key está correta

### Erro: "Package name already taken"
- O nome do pacote já existe no PyPI
- Escolha um nome diferente no campo `name`

## Workflow Recomendado

1. Faça suas alterações no código
2. Teste localmente
3. Incremente a versão
4. Commit e push das mudanças
5. Build e upload para PyPI
6. Crie uma tag no Git para a versão

```bash
git tag v0.2.0
git push origin v0.2.0
```

---

**Contato:** João Francisco de Souza Santos Lemos  
**Repositório:** https://github.com/Jfsslemos/Image2WorldLib