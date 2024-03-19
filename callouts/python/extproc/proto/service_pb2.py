# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rservice.proto\x12\x19\x65nvoy.service.ext_proc.v3\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xbf\x03\n\x11ProcessingRequest\x12\x12\n\nasync_mode\x18\x01 \x01(\x08\x12\x41\n\x0frequest_headers\x18\x02 \x01(\x0b\x32&.envoy.service.ext_proc.v3.HttpHeadersH\x00\x12\x42\n\x10response_headers\x18\x03 \x01(\x0b\x32&.envoy.service.ext_proc.v3.HttpHeadersH\x00\x12;\n\x0crequest_body\x18\x04 \x01(\x0b\x32#.envoy.service.ext_proc.v3.HttpBodyH\x00\x12<\n\rresponse_body\x18\x05 \x01(\x0b\x32#.envoy.service.ext_proc.v3.HttpBodyH\x00\x12\x43\n\x10request_trailers\x18\x06 \x01(\x0b\x32\'.envoy.service.ext_proc.v3.HttpTrailersH\x00\x12\x44\n\x11response_trailers\x18\x07 \x01(\x0b\x32\'.envoy.service.ext_proc.v3.HttpTrailersH\x00\x42\t\n\x07request"\xc3\x05\n\x12ProcessingResponse\x12\x45\n\x0frequest_headers\x18\x01 \x01(\x0b\x32*.envoy.service.ext_proc.v3.HeadersResponseH\x00\x12\x46\n\x10response_headers\x18\x02 \x01(\x0b\x32*.envoy.service.ext_proc.v3.HeadersResponseH\x00\x12?\n\x0crequest_body\x18\x03 \x01(\x0b\x32\'.envoy.service.ext_proc.v3.BodyResponseH\x00\x12@\n\rresponse_body\x18\x04 \x01(\x0b\x32\'.envoy.service.ext_proc.v3.BodyResponseH\x00\x12G\n\x10request_trailers\x18\x05 \x01(\x0b\x32+.envoy.service.ext_proc.v3.TrailersResponseH\x00\x12H\n\x11response_trailers\x18\x06 \x01(\x0b\x32+.envoy.service.ext_proc.v3.TrailersResponseH\x00\x12J\n\x12immediate_response\x18\x07 \x01(\x0b\x32,.envoy.service.ext_proc.v3.ImmediateResponseH\x00\x12\x31\n\x10\x64ynamic_metadata\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12@\n\rmode_override\x18\t \x01(\x0b\x32).envoy.service.ext_proc.v3.ProcessingMode\x12;\n\x18override_message_timeout\x18\n \x01(\x0b\x32\x19.google.protobuf.DurationB\n\n\x08response"\xf3\x01\n\x0bHttpHeaders\x12\x35\n\x07headers\x18\x01 \x01(\x0b\x32$.envoy.service.ext_proc.v3.HeaderMap\x12J\n\nattributes\x18\x02 \x03(\x0b\x32\x36.envoy.service.ext_proc.v3.HttpHeaders.AttributesEntry\x12\x15\n\rend_of_stream\x18\x03 \x01(\x08\x1aJ\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct:\x02\x38\x01"/\n\x08HttpBody\x12\x0c\n\x04\x62ody\x18\x01 \x01(\x0c\x12\x15\n\rend_of_stream\x18\x02 \x01(\x08"F\n\x0cHttpTrailers\x12\x36\n\x08trailers\x18\x01 \x01(\x0b\x32$.envoy.service.ext_proc.v3.HeaderMap"N\n\x0fHeadersResponse\x12;\n\x08response\x18\x01 \x01(\x0b\x32).envoy.service.ext_proc.v3.CommonResponse"V\n\x10TrailersResponse\x12\x42\n\x0fheader_mutation\x18\x01 \x01(\x0b\x32).envoy.service.ext_proc.v3.HeaderMutation"K\n\x0c\x42odyResponse\x12;\n\x08response\x18\x01 \x01(\x0b\x32).envoy.service.ext_proc.v3.CommonResponse"\xeb\x02\n\x0e\x43ommonResponse\x12H\n\x06status\x18\x01 \x01(\x0e\x32\x38.envoy.service.ext_proc.v3.CommonResponse.ResponseStatus\x12\x42\n\x0fheader_mutation\x18\x02 \x01(\x0b\x32).envoy.service.ext_proc.v3.HeaderMutation\x12>\n\rbody_mutation\x18\x03 \x01(\x0b\x32\'.envoy.service.ext_proc.v3.BodyMutation\x12\x36\n\x08trailers\x18\x04 \x01(\x0b\x32$.envoy.service.ext_proc.v3.HeaderMap\x12\x19\n\x11\x63lear_route_cache\x18\x05 \x01(\x08"8\n\x0eResponseStatus\x12\x0c\n\x08\x43ONTINUE\x10\x00\x12\x18\n\x14\x43ONTINUE_AND_REPLACE\x10\x01"\xe1\x01\n\x11ImmediateResponse\x12\x35\n\x06status\x18\x01 \x01(\x0b\x32%.envoy.service.ext_proc.v3.HttpStatus\x12:\n\x07headers\x18\x02 \x01(\x0b\x32).envoy.service.ext_proc.v3.HeaderMutation\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x12:\n\x0bgrpc_status\x18\x04 \x01(\x0b\x32%.envoy.service.ext_proc.v3.GrpcStatus\x12\x0f\n\x07\x64\x65tails\x18\x05 \x01(\t"\x1c\n\nGrpcStatus\x12\x0e\n\x06status\x18\x01 \x01(\r"k\n\x0eHeaderMutation\x12\x41\n\x0bset_headers\x18\x01 \x03(\x0b\x32,.envoy.service.ext_proc.v3.HeaderValueOption\x12\x16\n\x0eremove_headers\x18\x02 \x03(\t"@\n\x0c\x42odyMutation\x12\x0e\n\x04\x62ody\x18\x01 \x01(\x0cH\x00\x12\x14\n\nclear_body\x18\x02 \x01(\x08H\x00\x42\n\n\x08mutation"D\n\tHeaderMap\x12\x37\n\x07headers\x18\x01 \x03(\x0b\x32&.envoy.service.ext_proc.v3.HeaderValue"<\n\x0bHeaderValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\traw_value\x18\x03 \x01(\x0c"\xec\x02\n\x11HeaderValueOption\x12\x36\n\x06header\x18\x01 \x01(\x0b\x32&.envoy.service.ext_proc.v3.HeaderValue\x12.\n\x06\x61ppend\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x02\x18\x01\x12V\n\rappend_action\x18\x03 \x01(\x0e\x32?.envoy.service.ext_proc.v3.HeaderValueOption.HeaderAppendAction\x12\x18\n\x10keep_empty_value\x18\x04 \x01(\x08"}\n\x12HeaderAppendAction\x12\x1b\n\x17\x41PPEND_IF_EXISTS_OR_ADD\x10\x00\x12\x11\n\rADD_IF_ABSENT\x10\x01\x12\x1e\n\x1aOVERWRITE_IF_EXISTS_OR_ADD\x10\x02\x12\x17\n\x13OVERWRITE_IF_EXISTS\x10\x03"\x96\x05\n\x0eProcessingMode\x12U\n\x13request_header_mode\x18\x01 \x01(\x0e\x32\x38.envoy.service.ext_proc.v3.ProcessingMode.HeaderSendMode\x12V\n\x14response_header_mode\x18\x02 \x01(\x0e\x32\x38.envoy.service.ext_proc.v3.ProcessingMode.HeaderSendMode\x12Q\n\x11request_body_mode\x18\x03 \x01(\x0e\x32\x36.envoy.service.ext_proc.v3.ProcessingMode.BodySendMode\x12R\n\x12response_body_mode\x18\x04 \x01(\x0e\x32\x36.envoy.service.ext_proc.v3.ProcessingMode.BodySendMode\x12V\n\x14request_trailer_mode\x18\x05 \x01(\x0e\x32\x38.envoy.service.ext_proc.v3.ProcessingMode.HeaderSendMode\x12W\n\x15response_trailer_mode\x18\x06 \x01(\x0e\x32\x38.envoy.service.ext_proc.v3.ProcessingMode.HeaderSendMode"1\n\x0eHeaderSendMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x08\n\x04SEND\x10\x01\x12\x08\n\x04SKIP\x10\x02"J\n\x0c\x42odySendMode\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08STREAMED\x10\x01\x12\x0c\n\x08\x42UFFERED\x10\x02\x12\x14\n\x10\x42UFFERED_PARTIAL\x10\x03"A\n\nHttpStatus\x12\x33\n\x04\x63ode\x18\x01 \x01(\x0e\x32%.envoy.service.ext_proc.v3.StatusCode*\xb5\t\n\nStatusCode\x12\t\n\x05\x45mpty\x10\x00\x12\x0c\n\x08\x43ontinue\x10\x64\x12\x07\n\x02OK\x10\xc8\x01\x12\x0c\n\x07\x43reated\x10\xc9\x01\x12\r\n\x08\x41\x63\x63\x65pted\x10\xca\x01\x12 \n\x1bNonAuthoritativeInformation\x10\xcb\x01\x12\x0e\n\tNoContent\x10\xcc\x01\x12\x11\n\x0cResetContent\x10\xcd\x01\x12\x13\n\x0ePartialContent\x10\xce\x01\x12\x10\n\x0bMultiStatus\x10\xcf\x01\x12\x14\n\x0f\x41lreadyReported\x10\xd0\x01\x12\x0b\n\x06IMUsed\x10\xe2\x01\x12\x14\n\x0fMultipleChoices\x10\xac\x02\x12\x15\n\x10MovedPermanently\x10\xad\x02\x12\n\n\x05\x46ound\x10\xae\x02\x12\r\n\x08SeeOther\x10\xaf\x02\x12\x10\n\x0bNotModified\x10\xb0\x02\x12\r\n\x08UseProxy\x10\xb1\x02\x12\x16\n\x11TemporaryRedirect\x10\xb3\x02\x12\x16\n\x11PermanentRedirect\x10\xb4\x02\x12\x0f\n\nBadRequest\x10\x90\x03\x12\x11\n\x0cUnauthorized\x10\x91\x03\x12\x14\n\x0fPaymentRequired\x10\x92\x03\x12\x0e\n\tForbidden\x10\x93\x03\x12\r\n\x08NotFound\x10\x94\x03\x12\x15\n\x10MethodNotAllowed\x10\x95\x03\x12\x12\n\rNotAcceptable\x10\x96\x03\x12 \n\x1bProxyAuthenticationRequired\x10\x97\x03\x12\x13\n\x0eRequestTimeout\x10\x98\x03\x12\r\n\x08\x43onflict\x10\x99\x03\x12\t\n\x04Gone\x10\x9a\x03\x12\x13\n\x0eLengthRequired\x10\x9b\x03\x12\x17\n\x12PreconditionFailed\x10\x9c\x03\x12\x14\n\x0fPayloadTooLarge\x10\x9d\x03\x12\x0f\n\nURITooLong\x10\x9e\x03\x12\x19\n\x14UnsupportedMediaType\x10\x9f\x03\x12\x18\n\x13RangeNotSatisfiable\x10\xa0\x03\x12\x16\n\x11\x45xpectationFailed\x10\xa1\x03\x12\x17\n\x12MisdirectedRequest\x10\xa5\x03\x12\x18\n\x13UnprocessableEntity\x10\xa6\x03\x12\x0b\n\x06Locked\x10\xa7\x03\x12\x15\n\x10\x46\x61iledDependency\x10\xa8\x03\x12\x14\n\x0fUpgradeRequired\x10\xaa\x03\x12\x19\n\x14PreconditionRequired\x10\xac\x03\x12\x14\n\x0fTooManyRequests\x10\xad\x03\x12 \n\x1bRequestHeaderFieldsTooLarge\x10\xaf\x03\x12\x18\n\x13InternalServerError\x10\xf4\x03\x12\x13\n\x0eNotImplemented\x10\xf5\x03\x12\x0f\n\nBadGateway\x10\xf6\x03\x12\x17\n\x12ServiceUnavailable\x10\xf7\x03\x12\x13\n\x0eGatewayTimeout\x10\xf8\x03\x12\x1c\n\x17HTTPVersionNotSupported\x10\xf9\x03\x12\x1a\n\x15VariantAlsoNegotiates\x10\xfa\x03\x12\x18\n\x13InsufficientStorage\x10\xfb\x03\x12\x11\n\x0cLoopDetected\x10\xfc\x03\x12\x10\n\x0bNotExtended\x10\xfe\x03\x12"\n\x1dNetworkAuthenticationRequired\x10\xff\x03\x32\x81\x01\n\x11\x45xternalProcessor\x12l\n\x07Process\x12,.envoy.service.ext_proc.v3.ProcessingRequest\x1a-.envoy.service.ext_proc.v3.ProcessingResponse"\x00(\x01\x30\x01\x42\x43\n\'io.envoyproxy.envoy.service.ext_proc.v3B\x16\x45xternalProcessorProtoP\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "service_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n'io.envoyproxy.envoy.service.ext_proc.v3B\026ExternalProcessorProtoP\001"
    )
    _HTTPHEADERS_ATTRIBUTESENTRY._options = None
    _HTTPHEADERS_ATTRIBUTESENTRY._serialized_options = b"8\001"
    _HEADERVALUEOPTION.fields_by_name["append"]._options = None
    _HEADERVALUEOPTION.fields_by_name["append"]._serialized_options = b"\030\001"
    _globals["_STATUSCODE"]._serialized_start = 3941
    _globals["_STATUSCODE"]._serialized_end = 5146
    _globals["_PROCESSINGREQUEST"]._serialized_start = 139
    _globals["_PROCESSINGREQUEST"]._serialized_end = 586
    _globals["_PROCESSINGRESPONSE"]._serialized_start = 589
    _globals["_PROCESSINGRESPONSE"]._serialized_end = 1296
    _globals["_HTTPHEADERS"]._serialized_start = 1299
    _globals["_HTTPHEADERS"]._serialized_end = 1542
    _globals["_HTTPHEADERS_ATTRIBUTESENTRY"]._serialized_start = 1468
    _globals["_HTTPHEADERS_ATTRIBUTESENTRY"]._serialized_end = 1542
    _globals["_HTTPBODY"]._serialized_start = 1544
    _globals["_HTTPBODY"]._serialized_end = 1591
    _globals["_HTTPTRAILERS"]._serialized_start = 1593
    _globals["_HTTPTRAILERS"]._serialized_end = 1663
    _globals["_HEADERSRESPONSE"]._serialized_start = 1665
    _globals["_HEADERSRESPONSE"]._serialized_end = 1743
    _globals["_TRAILERSRESPONSE"]._serialized_start = 1745
    _globals["_TRAILERSRESPONSE"]._serialized_end = 1831
    _globals["_BODYRESPONSE"]._serialized_start = 1833
    _globals["_BODYRESPONSE"]._serialized_end = 1908
    _globals["_COMMONRESPONSE"]._serialized_start = 1911
    _globals["_COMMONRESPONSE"]._serialized_end = 2274
    _globals["_COMMONRESPONSE_RESPONSESTATUS"]._serialized_start = 2218
    _globals["_COMMONRESPONSE_RESPONSESTATUS"]._serialized_end = 2274
    _globals["_IMMEDIATERESPONSE"]._serialized_start = 2277
    _globals["_IMMEDIATERESPONSE"]._serialized_end = 2502
    _globals["_GRPCSTATUS"]._serialized_start = 2504
    _globals["_GRPCSTATUS"]._serialized_end = 2532
    _globals["_HEADERMUTATION"]._serialized_start = 2534
    _globals["_HEADERMUTATION"]._serialized_end = 2641
    _globals["_BODYMUTATION"]._serialized_start = 2643
    _globals["_BODYMUTATION"]._serialized_end = 2707
    _globals["_HEADERMAP"]._serialized_start = 2709
    _globals["_HEADERMAP"]._serialized_end = 2777
    _globals["_HEADERVALUE"]._serialized_start = 2779
    _globals["_HEADERVALUE"]._serialized_end = 2839
    _globals["_HEADERVALUEOPTION"]._serialized_start = 2842
    _globals["_HEADERVALUEOPTION"]._serialized_end = 3206
    _globals["_HEADERVALUEOPTION_HEADERAPPENDACTION"]._serialized_start = 3081
    _globals["_HEADERVALUEOPTION_HEADERAPPENDACTION"]._serialized_end = 3206
    _globals["_PROCESSINGMODE"]._serialized_start = 3209
    _globals["_PROCESSINGMODE"]._serialized_end = 3871
    _globals["_PROCESSINGMODE_HEADERSENDMODE"]._serialized_start = 3746
    _globals["_PROCESSINGMODE_HEADERSENDMODE"]._serialized_end = 3795
    _globals["_PROCESSINGMODE_BODYSENDMODE"]._serialized_start = 3797
    _globals["_PROCESSINGMODE_BODYSENDMODE"]._serialized_end = 3871
    _globals["_HTTPSTATUS"]._serialized_start = 3873
    _globals["_HTTPSTATUS"]._serialized_end = 3938
    _globals["_EXTERNALPROCESSOR"]._serialized_start = 5149
    _globals["_EXTERNALPROCESSOR"]._serialized_end = 5278
# @@protoc_insertion_point(module_scope)