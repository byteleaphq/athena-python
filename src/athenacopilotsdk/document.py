"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from athenacopilotsdk import utils
from athenacopilotsdk._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext
from athenacopilotsdk.models import components, errors, operations
from typing import Optional

class Document:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def post_document_brain_id_text(self, brain_id: str, request_body: Optional[operations.PostDocumentBrainIDTextRequestBody] = None) -> operations.PostDocumentBrainIDTextResponse:
        r"""Create Text Document"""
        hook_ctx = HookContext(operation_id='post_/document/{brain_id}/text', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.PostDocumentBrainIDTextRequest(
            brain_id=brain_id,
            request_body=request_body,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/document/{brain_id}/text', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.PostDocumentBrainIDTextRequest, "request_body", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.PostDocumentBrainIDTextResponse(http_meta=components.HTTPMetadata(request=req, response=http_res), headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDocumentBrainIDTextResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def post_document_brain_id_url(self, brain_id: str, request_body: Optional[operations.PostDocumentBrainIDURLRequestBody] = None) -> operations.PostDocumentBrainIDURLResponse:
        r"""Create Document by URL"""
        hook_ctx = HookContext(operation_id='post_/document/{brain_id}/url', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.PostDocumentBrainIDURLRequest(
            brain_id=brain_id,
            request_body=request_body,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/document/{brain_id}/url', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.PostDocumentBrainIDURLRequest, "request_body", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','500','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.PostDocumentBrainIDURLResponse(http_meta=components.HTTPMetadata(request=req, response=http_res), headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDocumentBrainIDURLResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 500:
            res.headers = http_res.headers
            
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.PostDocumentBrainIDURLResponseBody, infer_missing=True)
                out.http_meta = components.HTTPMetadata(request=req, response=http_res)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_document_brain_id_document_id_download(self, brain_id: str, document_id: str) -> operations.GetDocumentBrainIDDocumentIDDownloadResponse:
        r"""Download"""
        hook_ctx = HookContext(operation_id='get_/document/{brain_id}/{document_id}/download', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetDocumentBrainIDDocumentIDDownloadRequest(
            brain_id=brain_id,
            document_id=document_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/document/{brain_id}/{document_id}/download', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.GetDocumentBrainIDDocumentIDDownloadResponse(http_meta=components.HTTPMetadata(request=req, response=http_res), headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetDocumentBrainIDDocumentIDDownloadResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_document_brain_id_(self, brain_id: str) -> operations.GetDocumentBrainIDResponse:
        r"""List Documents"""
        hook_ctx = HookContext(operation_id='get_/document/{brain_id}', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetDocumentBrainIDRequest(
            brain_id=brain_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/document/{brain_id}', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.GetDocumentBrainIDResponse(http_meta=components.HTTPMetadata(request=req, response=http_res), headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetDocumentBrainIDResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_document_brain_id_document_id_(self, brain_id: str, document_id: str) -> operations.GetDocumentBrainIDDocumentIDResponse:
        r"""Get Document"""
        hook_ctx = HookContext(operation_id='get_/document/{brain_id}/{document_id}', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetDocumentBrainIDDocumentIDRequest(
            brain_id=brain_id,
            document_id=document_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/document/{brain_id}/{document_id}', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.GetDocumentBrainIDDocumentIDResponse(http_meta=components.HTTPMetadata(request=req, response=http_res), headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetDocumentBrainIDDocumentIDResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def delete_document_brain_id_document_id_(self, brain_id: str, document_id: str) -> operations.DeleteDocumentBrainIDDocumentIDResponse:
        r"""Delete Document"""
        hook_ctx = HookContext(operation_id='delete_/document/{brain_id}/{document_id}', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.DeleteDocumentBrainIDDocumentIDRequest(
            brain_id=brain_id,
            document_id=document_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/document/{brain_id}/{document_id}', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('DELETE', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.DeleteDocumentBrainIDDocumentIDResponse(http_meta=components.HTTPMetadata(request=req, response=http_res), headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteDocumentBrainIDDocumentIDResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def post_document_brain_id_file(self, brain_id: str, request_body: Optional[operations.PostDocumentBrainIDFileRequestBody] = None) -> operations.PostDocumentBrainIDFileResponse:
        r"""Upload Document"""
        hook_ctx = HookContext(operation_id='post_/document/{brain_id}/file', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.PostDocumentBrainIDFileRequest(
            brain_id=brain_id,
            request_body=request_body,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/document/{brain_id}/file', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        req_content_type, data, form = utils.serialize_request_body(request, operations.PostDocumentBrainIDFileRequest, "request_body", False, True, 'multipart')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.PostDocumentBrainIDFileResponse(http_meta=components.HTTPMetadata(request=req, response=http_res), headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostDocumentBrainIDFileResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    

