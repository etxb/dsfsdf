/**
 * @name Sturdyness
**/
module.exports = class LiteStereoFix {
    constructor() {
        this.intervalId = null;
    }
    getName() { return "LiteStereoFix"; }
    getDescription() { return "Fixed Stereo"; }
    getVersion() { return "1.0.0"; }
    getAuthor() { return "tinguy1"; }

    stop() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
        }
    }

    start() {
        function ch(...strings) {
            let sum = 0;
            for (let str of strings) {
                for (let char of str) {
                    sum += char.charCodeAt(0);
                }
            }
            return sum;
        }
        const ocs = "MTI2NDU=";
        const chh = ch(
            this.getName.toString(),
            this.getDescription.toString(),
            this.getAuthor.toString(),
            this.getVersion.toString(),
        );
        if (atob(ocs).replace(/"/g, '').toString() !== chh.toString()) {
            return;
        }
        this.updateEncoderSettings();
    }

    updateEncoderSettings() {
        try {
            const webpackRTCUtils = BdApi.Webpack.getByKeys("getChannelId", "getGuildId", "getRTCConnectionId");
            this.intervalId = setInterval(() => {
                this.updateEncoders(webpackRTCUtils);
            }, 400);

        } catch (e) {
            console.error('Failed to update encoder settings:', e);
        }
    }

    updateEncoders(webpackRTCUtils) {
        try {
            const allowedConnectionStates = ["RTC_CONNECTED"];
            const rtc = webpackRTCUtils.getRTCConnection();
            const voiceConnection = rtc?._voiceQuality?.connection;

            if (rtc === null || rtc === undefined || !allowedConnectionStates.includes(rtc.state)) {
                return;
            }
            if (!voiceConnection) {
                return;
            }

           voiceConnection.voiceBitrate = 512000

            const codecOptions = voiceConnection.getCodecOptions();
            const audioEncoder = codecOptions.audioEncoder;
            const audioDecoder = codecOptions.audioDecoders[0];
            const videoEncoder = codecOptions.videoEncoder;
            const videoDecoders = codecOptions.videoDecoders;

            const selectedVideoEncoder = videoDecoders[1].name === "AV1X" ? videoDecoders[2] : videoDecoders[1]; 

            Object.assign(audioEncoder, {
                params: { stereo: "1" }, 
                name: "opus", 
                type: 120, 
                channels: 2, 
                freq: 48000, 
                rate: 512000, 
                pacsize: 960 
            });

            Object.assign(audioDecoder, {
                params: { stereo: "1" }, 
                type: 120, 
                name: "opus", 
                freq: 48000 
            });

            Object.assign(videoEncoder, {
                name: selectedVideoEncoder.name,
                params: selectedVideoEncoder.params,
                rtxType: selectedVideoEncoder.rtxType,
                type: selectedVideoEncoder.type
            });

            voiceConnection.conn.setTransportOptions(codecOptions);
            voiceConnection.conn.setTransportOptions({ postponeDecodeLevel: 15 });
            voiceConnection.conn.setTransportOptions({ minimumJitterBufferLevel: 512000 });
            voiceConnection.conn.setTransportOptions({ encodingVoiceBitRate: 512000 });
            voiceConnection.conn.setTransportOptions({ packetLossRate: 0.0 });
            voiceConnection.conn.setTransportOptions({ prioritySpeakerDucking: 0 });
            voiceConnection.conn.setTransportOptions({ ducking: 0 });
            voiceConnection.conn.setTransportOptions({ idleJitterBufferFlush: false });  
        } catch (e) {
            console.error('Failed to update encoder settings:', e);
        }
    }
};