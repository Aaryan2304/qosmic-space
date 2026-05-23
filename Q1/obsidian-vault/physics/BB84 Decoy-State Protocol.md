---
type: physics
name: BB84 Decoy-State Protocol
domain: quantum
description: A QKD protocol using decoy pulses of varying intensity to detect photon-number-splitting attacks. Alice sends weak coherent pulses at three intensity levels; Bob and Alice use decoy statistics to bound eavesdropper information.
key_equations: "R >= q { -Q_mu f(E_mu) H_2(E_mu) + Q_1 [1 - H_2(e_1)] }  (asymptotic key rate lower bound)"
---

# BB84 Decoy-State Protocol

## Description

BB84 uses polarization states of single photons to encode key bits. Alice prepares photons in one of four polarization states; Bob measures in a randomly chosen basis. After transmission, they reconcile bases and perform error correction and privacy amplification.

In practice, weak coherent pulses (attenuated laser) replace single photons. Multi-photon pulses are vulnerable to photon-number-splitting attacks. The decoy-state method solves this: Alice randomly varies pulse intensity between signal, decoy, and vacuum levels. By comparing detection rates at each level, Alice and Bob can detect PNS attacks and bound Eve's information.

## Key Equations

- Photon number distribution: P(n, mu) = mu^n e^{-mu} / n!
- Gain: Q_mu = 1 - e^{-eta mu}
- Key rate: R >= q { -Q_mu f(E_mu) H_2(E_mu) + Q_1 [1 - H_2(e_1)] }

## Relevance to QOSMIC

QOSMIC's ground stations are designed to support both classical laser communication and quantum key distribution. The BB84 decoy-state protocol is our baseline QKD protocol because it is compatible with weak coherent pulse sources (no single-photon source needed) and has been demonstrated in multiple satellite-to-ground experiments, including the Chinese Micius satellite and the European Eagle-1 mission.

Our receiver uses fiber-coupled InGaAs single-photon detectors that are compatible with the decoy-state protocol's requirement for photon-number-resolving or threshold detection at 1550 nm.

## Related Decisions

- [[Single-Mode vs Multi-Mode Fiber Coupling]]

## References

- [[InGaAs Single-Photon Detector Module]]
- [[Cailabs OGS Technical Reference]]
