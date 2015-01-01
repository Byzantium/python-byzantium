""" Ripped from the network manager C api header files """


NMState = {
            'NM_STATE_UNKNOWN         ':0,
            'NM_STATE_ASLEEP          ':10,
            'NM_STATE_DISCONNECTED    ':20,
            'NM_STATE_DISCONNECTING   ':30,
            'NM_STATE_CONNECTING      ':40,
            'NM_STATE_CONNECTED_LOCAL ':50,
            'NM_STATE_CONNECTED_SITE  ':60,
            'NM_STATE_CONNECTED_GLOBAL':70
            }

NMConnectivityState = {}
"""missing values
                    'NM_CONNECTIVITY_UNKNOWN':?,
                    'NM_CONNECTIVITY_NONE':?,
                    'NM_CONNECTIVITY_PORTAL':?,
                    'NM_CONNECTIVITY_LIMITED':?,
                    'NM_CONNECTIVITY_FULL':?
                    }"""

NMDeviceType = {
                'NM_DEVICE_TYPE_UNKNOWN   ':0,
                'NM_DEVICE_TYPE_ETHERNET  ':1,
                'NM_DEVICE_TYPE_WIFI      ':2,
                'NM_DEVICE_TYPE_UNUSED1   ':3,
                'NM_DEVICE_TYPE_UNUSED2   ':4,
                'NM_DEVICE_TYPE_OLPC_MESH ':6,
                'NM_DEVICE_TYPE_WIMAX     ':7,
                'NM_DEVICE_TYPE_MODEM     ':8,
                'NM_DEVICE_TYPE_INFINIBAND':9,
                'NM_DEVICE_TYPE_BOND      ':10,
                'NM_DEVICE_TYPE_VLAN      ':11,
                'NM_DEVICE_TYPE_ADSL      ':12,
                'NM_DEVICE_TYPE_BRIDGE    ':13,
                'NM_DEVICE_TYPE_GENERIC   ':14,
                'NM_DEVICE_TYPE_TEAM      ':15,
                }

NMDeviceCapabilities = {
                        'NM_DEVICE_CAP_NONE          ':0x00000000,
                        'NM_DEVICE_CAP_NM_SUPPORTED  ':0x00000001,
                        'NM_DEVICE_CAP_CARRIER_DETECT':0x00000002
                        }


NMDeviceCapabilities = {
                        'NM_WIFI_DEVICE_CAP_NONE         ':0x00000000,
                        'NM_WIFI_DEVICE_CAP_CIPHER_WEP40 ':0x00000001,
                        'NM_WIFI_DEVICE_CAP_CIPHER_WEP104':0x00000002,
                        'NM_WIFI_DEVICE_CAP_CIPHER_TKIP  ':0x00000004,
                        'NM_WIFI_DEVICE_CAP_CIPHER_CCMP  ':0x00000008,
                        'NM_WIFI_DEVICE_CAP_WPA          ':0x00000010,
                        'NM_WIFI_DEVICE_CAP_RSN          ':0x00000020,
                        'NM_WIFI_DEVICE_CAP_AP           ':0x00000040,
                        'NM_WIFI_DEVICE_CAP_ADHOC        ':0x00000080
                        }


NMDeviceCapabilities = {
                    'NM_802_11_AP_FLAGS_NONE   ':0x00000000,
                    'NM_802_11_AP_FLAGS_PRIVACY':0x00000001
                    }

NMDeviceCapabilities = {
                    'NM_802_11_AP_SEC_NONE           ':0x00000000,
                    'NM_802_11_AP_SEC_PAIR_WEP40     ':0x00000001,
                    'NM_802_11_AP_SEC_PAIR_WEP104    ':0x00000002,
                    'NM_802_11_AP_SEC_PAIR_TKIP      ':0x00000004,
                    'NM_802_11_AP_SEC_PAIR_CCMP      ':0x00000008,
                    'NM_802_11_AP_SEC_GROUP_WEP40    ':0x00000010,
                    'NM_802_11_AP_SEC_GROUP_WEP104   ':0x00000020,
                    'NM_802_11_AP_SEC_GROUP_TKIP     ':0x00000040,
                    'NM_802_11_AP_SEC_GROUP_CCMP     ':0x00000080,
                    'NM_802_11_AP_SEC_KEY_MGMT_PSK   ':0x00000100,
                    'NM_802_11_AP_SEC_KEY_MGMT_802_1X':0x00000200
                    }

NM80211Mode = {}
"""missing values
            'NM_802_11_MODE_UNKNOWN':0,
            'NM_802_11_MODE_ADHOC':?,
            'NM_802_11_MODE_INFRA':?,
            'NM_802_11_MODE_AP':?
            }"""

NMBluetoothCapabilities = {
                        'NM_BT_CAPABILITY_NONE':0x00000000,
                        'NM_BT_CAPABILITY_DUN ':0x00000001,
                        'NM_BT_CAPABILITY_NAP ':0x00000002,
                        }

NMDeviceModemCapabilities = {
                        'NM_DEVICE_MODEM_CAPABILITY_NONE     ':0x00000000,
                        'NM_DEVICE_MODEM_CAPABILITY_POTS     ':0x00000001,
                        'NM_DEVICE_MODEM_CAPABILITY_CDMA_EVDO':0x00000002,
                        'NM_DEVICE_MODEM_CAPABILITY_GSM_UMTS ':0x00000004,
                        'NM_DEVICE_MODEM_CAPABILITY_LTE      ':0x00000008,
                        }

NMDeviceState = {
                'NM_DEVICE_STATE_UNKNOWN     ':0,
                'NM_DEVICE_STATE_UNMANAGED   ':10,
                'NM_DEVICE_STATE_UNAVAILABLE ':20,
                'NM_DEVICE_STATE_DISCONNECTED':30,
                'NM_DEVICE_STATE_PREPARE     ':40,
                'NM_DEVICE_STATE_CONFIG      ':50,
                'NM_DEVICE_STATE_NEED_AUTH   ':60,
                'NM_DEVICE_STATE_IP_CONFIG   ':70,
                'NM_DEVICE_STATE_IP_CHECK    ':80,
                'NM_DEVICE_STATE_SECONDARIES ':90,
                'NM_DEVICE_STATE_ACTIVATED   ':100,
                'NM_DEVICE_STATE_DEACTIVATING':110,
                'NM_DEVICE_STATE_FAILED      ':120
                }


NMDeviceStateReason = {
                    'NM_DEVICE_STATE_REASON_NONE':0,
                    'NM_DEVICE_STATE_REASON_UNKNOWN':1,
                    'NM_DEVICE_STATE_REASON_NOW_MANAGED':2,
                    'NM_DEVICE_STATE_REASON_NOW_UNMANAGED':3,
                    'NM_DEVICE_STATE_REASON_CONFIG_FAILED':4,
                    'NM_DEVICE_STATE_REASON_IP_CONFIG_UNAVAILABLE':5,
                    'NM_DEVICE_STATE_REASON_IP_CONFIG_EXPIRED':6,
                    'NM_DEVICE_STATE_REASON_NO_SECRETS':7,
                    'NM_DEVICE_STATE_REASON_SUPPLICANT_DISCONNECT':8,
                    'NM_DEVICE_STATE_REASON_SUPPLICANT_CONFIG_FAILED':9,
                    'NM_DEVICE_STATE_REASON_SUPPLICANT_FAILED':10,
                    'NM_DEVICE_STATE_REASON_SUPPLICANT_TIMEOUT':11,
                    'NM_DEVICE_STATE_REASON_PPP_START_FAILED':12,
                    'NM_DEVICE_STATE_REASON_PPP_DISCONNECT':13,
                    'NM_DEVICE_STATE_REASON_PPP_FAILED':14,
                    'NM_DEVICE_STATE_REASON_DHCP_START_FAILED':15,
                    'NM_DEVICE_STATE_REASON_DHCP_ERROR':16,
                    'NM_DEVICE_STATE_REASON_DHCP_FAILED':17,
                    'NM_DEVICE_STATE_REASON_SHARED_START_FAILED':18,
                    'NM_DEVICE_STATE_REASON_SHARED_FAILED':19,
                    'NM_DEVICE_STATE_REASON_AUTOIP_START_FAILED':20,
                    'NM_DEVICE_STATE_REASON_AUTOIP_ERROR':21,
                    'NM_DEVICE_STATE_REASON_AUTOIP_FAILED':22,
                    'NM_DEVICE_STATE_REASON_MODEM_BUSY':23,
                    'NM_DEVICE_STATE_REASON_MODEM_NO_DIAL_TONE':24,
                    'NM_DEVICE_STATE_REASON_MODEM_NO_CARRIER':25,
                    'NM_DEVICE_STATE_REASON_MODEM_DIAL_TIMEOUT':26,
                    'NM_DEVICE_STATE_REASON_MODEM_DIAL_FAILED':27,
                    'NM_DEVICE_STATE_REASON_MODEM_INIT_FAILED':28,
                    'NM_DEVICE_STATE_REASON_GSM_APN_FAILED':29,
                    'NM_DEVICE_STATE_REASON_GSM_REGISTRATION_NOT_SEARCHING':30,
                    'NM_DEVICE_STATE_REASON_GSM_REGISTRATION_DENIED':31,
                    'NM_DEVICE_STATE_REASON_GSM_REGISTRATION_TIMEOUT':32,
                    'NM_DEVICE_STATE_REASON_GSM_REGISTRATION_FAILED':33,
                    'NM_DEVICE_STATE_REASON_GSM_PIN_CHECK_FAILED':34,
                    'NM_DEVICE_STATE_REASON_FIRMWARE_MISSING':35,
                    'NM_DEVICE_STATE_REASON_REMOVED':36,
                    'NM_DEVICE_STATE_REASON_SLEEPING':37,
                    'NM_DEVICE_STATE_REASON_CONNECTION_REMOVED':38,
                    'NM_DEVICE_STATE_REASON_USER_REQUESTED':39,
                    'NM_DEVICE_STATE_REASON_CARRIER':40,
                    'NM_DEVICE_STATE_REASON_CONNECTION_ASSUMED':41,
                    'NM_DEVICE_STATE_REASON_SUPPLICANT_AVAILABLE':42,
                    'NM_DEVICE_STATE_REASON_MODEM_NOT_FOUND':43,
                    'NM_DEVICE_STATE_REASON_BT_FAILED':44,
                    'NM_DEVICE_STATE_REASON_GSM_SIM_NOT_INSERTED':45,
                    'NM_DEVICE_STATE_REASON_GSM_SIM_PIN_REQUIRED':46,
                    'NM_DEVICE_STATE_REASON_GSM_SIM_PUK_REQUIRED':47,
                    'NM_DEVICE_STATE_REASON_GSM_SIM_WRONG':48,
                    'NM_DEVICE_STATE_REASON_INFINIBAND_MODE':49,
                    'NM_DEVICE_STATE_REASON_DEPENDENCY_FAILED':50,
                    'NM_DEVICE_STATE_REASON_BR2684_FAILED':51,
                    'NM_DEVICE_STATE_REASON_MODEM_MANAGER_UNAVAILABLE':52,
                    'NM_DEVICE_STATE_REASON_SSID_NOT_FOUND':53,
                    'NM_DEVICE_STATE_REASON_SECONDARY_CONNECTION_FAILED':54,
                    'NM_DEVICE_STATE_REASON_DCB_FCOE_FAILED':55,
                    'NM_DEVICE_STATE_REASON_TEAMD_CONTROL_FAILED':56,
                    'NM_DEVICE_STATE_REASON_MODEM_FAILED':57,
                    'NM_DEVICE_STATE_REASON_MODEM_AVAILABLE':58,
                    'NM_DEVICE_STATE_REASON_SIM_PIN_INCORRECT':59,
                    'NM_DEVICE_STATE_REASON_LAST':0xFFFF
                    }


NMDeviceStateReason = {}
""" missing values
                    'NM_ACTIVE_CONNECTION_STATE_UNKNOWN':0,
                    'NM_ACTIVE_CONNECTION_STATE_ACTIVATING':?,
                    'NM_ACTIVE_CONNECTION_STATE_ACTIVATED':?,
                    'NM_ACTIVE_CONNECTION_STATE_DEACTIVATING':?,
                    'NM_ACTIVE_CONNECTION_STATE_DEACTIVATED':?
                    }"""


