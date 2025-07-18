# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T15:00:48+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    EgcerCertificatePostRequest,
    EgcerCertificatePostResponse,
    EgcerCertificatePostResponse1,
    EgcerCertificatePostResponse2,
    EgcerCertificatePostResponse3,
    EgcerCertificatePostResponse4,
    EgcerCertificatePostResponse5,
    EgcerCertificatePostResponse6,
    EwcerCertificatePostRequest,
    EwcerCertificatePostResponse,
    EwcerCertificatePostResponse1,
    EwcerCertificatePostResponse2,
    EwcerCertificatePostResponse3,
    EwcerCertificatePostResponse4,
    EwcerCertificatePostResponse5,
    EwcerCertificatePostResponse6,
    IncerCertificatePostRequest,
    IncerCertificatePostResponse,
    IncerCertificatePostResponse1,
    IncerCertificatePostResponse2,
    IncerCertificatePostResponse3,
    IncerCertificatePostResponse4,
    IncerCertificatePostResponse5,
    IncerCertificatePostResponse6,
    LhcerCertificatePostRequest,
    LhcerCertificatePostResponse,
    LhcerCertificatePostResponse1,
    LhcerCertificatePostResponse2,
    LhcerCertificatePostResponse3,
    LhcerCertificatePostResponse4,
    LhcerCertificatePostResponse5,
    LhcerCertificatePostResponse6,
    ObcerCertificatePostRequest,
    ObcerCertificatePostResponse,
    ObcerCertificatePostResponse1,
    ObcerCertificatePostResponse2,
    ObcerCertificatePostResponse3,
    ObcerCertificatePostResponse4,
    ObcerCertificatePostResponse5,
    ObcerCertificatePostResponse6,
    RscerCertificatePostRequest,
    RscerCertificatePostResponse,
    RscerCertificatePostResponse1,
    RscerCertificatePostResponse2,
    RscerCertificatePostResponse3,
    RscerCertificatePostResponse4,
    RscerCertificatePostResponse5,
    RscerCertificatePostResponse6,
    ShcerCertificatePostRequest,
    ShcerCertificatePostResponse,
    ShcerCertificatePostResponse1,
    ShcerCertificatePostResponse2,
    ShcerCertificatePostResponse3,
    ShcerCertificatePostResponse4,
    ShcerCertificatePostResponse5,
    ShcerCertificatePostResponse6,
)

app = MCPProxy(
    description='APIs provided by eDistrict Odisha ServicePlus, Odisha.',
    termsOfService='https://apisetu.gov.in/terms.php',
    title='eDistrict Odisha ServicePlus, Odisha',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/edistrictodishasp/v3'}],
)


@app.post(
    '/egcer/certificate',
    description=""" API to verify Economically Backward In General Caste Certificate. """,
    tags=['certificate_processing'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def egcer(body: EgcerCertificatePostRequest = None):
    """
    Economically Backward In General Caste Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/ewcer/certificate',
    description=""" API to verify Economically Weaker Section Certificate. """,
    tags=['certificate_processing'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def ewcer(body: EwcerCertificatePostRequest = None):
    """
    Economically Weaker Section Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/incer/certificate',
    description=""" API to verify Income Certificate. """,
    tags=['certificate_processing'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def incer(body: IncerCertificatePostRequest = None):
    """
    Income Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/lhcer/certificate',
    description=""" API to verify Legal Heir Certificate. """,
    tags=['certificate_processing'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def lhcer(body: LhcerCertificatePostRequest = None):
    """
    Legal Heir Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/obcer/certificate',
    description=""" API to verify OBC Certificate. """,
    tags=['certificate_processing'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def obcer(body: ObcerCertificatePostRequest = None):
    """
    OBC Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/rscer/certificate',
    description=""" API to verify Residence Certificate. """,
    tags=['certificate_processing'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def rscer(body: RscerCertificatePostRequest = None):
    """
    Residence Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/shcer/certificate',
    description=""" API to verify SC/ST  Certificate. """,
    tags=['certificate_processing'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def shcer(body: ShcerCertificatePostRequest = None):
    """
    SC/ST  Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
