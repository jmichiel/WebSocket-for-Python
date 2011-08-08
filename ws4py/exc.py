# -*- coding: utf-8 -*-

__all__ = ['WebSocketException', 'FrameTooLargeException', 'ProtocolException',
           'FUnsupportedFrameTypeException', 'TextFrameEncodingException',
           'StreamClosed', 'HandshakeError']

class WebSocketException(Exception): pass

class ProtocolException(WebSocketException): pass

class FrameTooLargeException(WebSocketException): pass

class UnsupportedFrameTypeException(WebSocketException): pass

class TextFrameEncodingException(WebSocketException): pass

class StreamClosed(Exception): pass

class HandshakeError(WebSocketException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
