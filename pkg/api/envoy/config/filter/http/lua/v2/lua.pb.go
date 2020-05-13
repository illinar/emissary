// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: envoy/config/filter/http/lua/v2/lua.proto

package envoy_config_filter_http_lua_v2

import (
	fmt "fmt"
	_ "github.com/cncf/udpa/go/udpa/annotations"
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
	proto "github.com/gogo/protobuf/proto"
	io "io"
	math "math"
	math_bits "math/bits"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.GoGoProtoPackageIsVersion3 // please upgrade the proto package

type Lua struct {
	// The Lua code that Envoy will execute. This can be a very small script that
	// further loads code from disk if desired. Note that if JSON configuration is used, the code must
	// be properly escaped. YAML configuration may be easier to read since YAML supports multi-line
	// strings so complex scripts can be easily expressed inline in the configuration.
	InlineCode           string   `protobuf:"bytes,1,opt,name=inline_code,json=inlineCode,proto3" json:"inline_code,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Lua) Reset()         { *m = Lua{} }
func (m *Lua) String() string { return proto.CompactTextString(m) }
func (*Lua) ProtoMessage()    {}
func (*Lua) Descriptor() ([]byte, []int) {
	return fileDescriptor_f59dca3e63e33613, []int{0}
}
func (m *Lua) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *Lua) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_Lua.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *Lua) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Lua.Merge(m, src)
}
func (m *Lua) XXX_Size() int {
	return m.Size()
}
func (m *Lua) XXX_DiscardUnknown() {
	xxx_messageInfo_Lua.DiscardUnknown(m)
}

var xxx_messageInfo_Lua proto.InternalMessageInfo

func (m *Lua) GetInlineCode() string {
	if m != nil {
		return m.InlineCode
	}
	return ""
}

func init() {
	proto.RegisterType((*Lua)(nil), "envoy.config.filter.http.lua.v2.Lua")
}

func init() {
	proto.RegisterFile("envoy/config/filter/http/lua/v2/lua.proto", fileDescriptor_f59dca3e63e33613)
}

var fileDescriptor_f59dca3e63e33613 = []byte{
	// 261 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xd2, 0x4c, 0xcd, 0x2b, 0xcb,
	0xaf, 0xd4, 0x4f, 0xce, 0xcf, 0x4b, 0xcb, 0x4c, 0xd7, 0x4f, 0xcb, 0xcc, 0x29, 0x49, 0x2d, 0xd2,
	0xcf, 0x28, 0x29, 0x29, 0xd0, 0xcf, 0x29, 0x4d, 0xd4, 0x2f, 0x33, 0x02, 0x51, 0x7a, 0x05, 0x45,
	0xf9, 0x25, 0xf9, 0x42, 0xf2, 0x60, 0xa5, 0x7a, 0x10, 0xa5, 0x7a, 0x10, 0xa5, 0x7a, 0x20, 0xa5,
	0x7a, 0x20, 0x35, 0x65, 0x46, 0x52, 0x72, 0xa5, 0x29, 0x05, 0x89, 0xfa, 0x89, 0x79, 0x79, 0xf9,
	0x25, 0x89, 0x25, 0x99, 0xf9, 0x79, 0xc5, 0xfa, 0xb9, 0x99, 0xe9, 0x45, 0x89, 0x25, 0xa9, 0x10,
	0x03, 0xa4, 0x64, 0x31, 0xe4, 0x8b, 0x4b, 0x12, 0x4b, 0x4a, 0x8b, 0xa1, 0xd2, 0xe2, 0x65, 0x89,
	0x39, 0x99, 0x29, 0x89, 0x25, 0xa9, 0xfa, 0x30, 0x06, 0x44, 0x42, 0x49, 0x9f, 0x8b, 0xd9, 0xa7,
	0x34, 0x51, 0x48, 0x83, 0x8b, 0x3b, 0x33, 0x2f, 0x27, 0x33, 0x2f, 0x35, 0x3e, 0x39, 0x3f, 0x25,
	0x55, 0x82, 0x51, 0x81, 0x51, 0x83, 0xd3, 0x89, 0xfd, 0x97, 0x13, 0x4b, 0x11, 0x93, 0x02, 0x63,
	0x10, 0x17, 0x44, 0xce, 0x39, 0x3f, 0x25, 0xd5, 0xa9, 0xfa, 0xc4, 0x23, 0x39, 0xc6, 0x0b, 0x8f,
	0xe4, 0x18, 0x1f, 0x3c, 0x92, 0x63, 0xfc, 0x34, 0xe3, 0x5f, 0x3f, 0xab, 0x9a, 0x90, 0x0a, 0xc4,
	0xf5, 0xa9, 0x15, 0x25, 0xa9, 0x79, 0xc5, 0x20, 0xcb, 0xa1, 0x3e, 0x28, 0x46, 0xf2, 0x82, 0xf1,
	0xae, 0x86, 0x13, 0x17, 0xd9, 0x98, 0x04, 0x18, 0xb8, 0x74, 0x33, 0xf3, 0xf5, 0xc0, 0x1a, 0x0a,
	0x8a, 0xf2, 0x2b, 0x2a, 0xf5, 0x08, 0xf8, 0xdc, 0x89, 0xc3, 0xa7, 0x34, 0x31, 0x00, 0xe4, 0xd6,
	0x00, 0xc6, 0x24, 0x36, 0xb0, 0xa3, 0x8d, 0x01, 0x01, 0x00, 0x00, 0xff, 0xff, 0xd6, 0x06, 0xd0,
	0xbb, 0x5a, 0x01, 0x00, 0x00,
}

func (m *Lua) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *Lua) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *Lua) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if len(m.InlineCode) > 0 {
		i -= len(m.InlineCode)
		copy(dAtA[i:], m.InlineCode)
		i = encodeVarintLua(dAtA, i, uint64(len(m.InlineCode)))
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func encodeVarintLua(dAtA []byte, offset int, v uint64) int {
	offset -= sovLua(v)
	base := offset
	for v >= 1<<7 {
		dAtA[offset] = uint8(v&0x7f | 0x80)
		v >>= 7
		offset++
	}
	dAtA[offset] = uint8(v)
	return base
}
func (m *Lua) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	l = len(m.InlineCode)
	if l > 0 {
		n += 1 + l + sovLua(uint64(l))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func sovLua(x uint64) (n int) {
	return (math_bits.Len64(x|1) + 6) / 7
}
func sozLua(x uint64) (n int) {
	return sovLua(uint64((x << 1) ^ uint64((int64(x) >> 63))))
}
func (m *Lua) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowLua
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: Lua: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: Lua: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field InlineCode", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowLua
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthLua
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthLua
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.InlineCode = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipLua(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthLua
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthLua
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func skipLua(dAtA []byte) (n int, err error) {
	l := len(dAtA)
	iNdEx := 0
	depth := 0
	for iNdEx < l {
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return 0, ErrIntOverflowLua
			}
			if iNdEx >= l {
				return 0, io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= (uint64(b) & 0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		wireType := int(wire & 0x7)
		switch wireType {
		case 0:
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowLua
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				iNdEx++
				if dAtA[iNdEx-1] < 0x80 {
					break
				}
			}
		case 1:
			iNdEx += 8
		case 2:
			var length int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowLua
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				length |= (int(b) & 0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if length < 0 {
				return 0, ErrInvalidLengthLua
			}
			iNdEx += length
		case 3:
			depth++
		case 4:
			if depth == 0 {
				return 0, ErrUnexpectedEndOfGroupLua
			}
			depth--
		case 5:
			iNdEx += 4
		default:
			return 0, fmt.Errorf("proto: illegal wireType %d", wireType)
		}
		if iNdEx < 0 {
			return 0, ErrInvalidLengthLua
		}
		if depth == 0 {
			return iNdEx, nil
		}
	}
	return 0, io.ErrUnexpectedEOF
}

var (
	ErrInvalidLengthLua        = fmt.Errorf("proto: negative length found during unmarshaling")
	ErrIntOverflowLua          = fmt.Errorf("proto: integer overflow")
	ErrUnexpectedEndOfGroupLua = fmt.Errorf("proto: unexpected end of group")
)
