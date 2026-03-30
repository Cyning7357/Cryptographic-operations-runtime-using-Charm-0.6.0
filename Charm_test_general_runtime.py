from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair,hashPair
from charm.toolbox.ecgroup import ECGroup,ZR,G
from charm.toolbox.eccurve import secp256k1
import os
import time
count = 1000


print("==========Testing Bilinear Pairing==========")

group=PairingGroup('BN254')

total_add_G1 = 0
for i in range (count):
    P=group.random(G1)
    Q=group.random(G1)
    start = time.perf_counter()
    R = P * Q
    end = time.perf_counter()
    total_add_G1 += end-start
print("total time in G_1 of (g^a * g^b) or (g^a + g^b) = ",total_add_G1," s.")

total_exp_G1 = 0
for i in range (count):
    P=group.random(G1)
    x = group.random(ZR)
    start = time.perf_counter()
    R = P ** x
    end = time.perf_counter()
    total_exp_G1 += end-start
print("total time in G_1 of g^a = ",total_exp_G1," s.")

total_map_G1 = 0
for i in range (count):
    msg = os.urandom(32)
    start = time.perf_counter()
    P = group.hash(msg,G1)
    end = time.perf_counter()
    total_map_G1 += end - start
print("total time in G_1 of map to point operation = ",total_map_G1," s.")

total_mul_G2 = 0
for i in range (count):
    P=group.random(G2)
    Q=group.random(G2)
    start = time.perf_counter()
    R = P * Q
    end = time.perf_counter()
    total_mul_G2 += end-start
print("total time in G_2 of (g^a * g^b) or (g^a + g^b) = ",total_mul_G2," s.")

total_exp_G2 = 0
for i in range (count):
    P=group.random(G2)
    x = group.random(ZR)
    start = time.perf_counter()
    R = P ** x
    end = time.perf_counter()
    total_exp_G2 += end-start
print("total time in G_2 of g^a = ",total_exp_G2," s.")

total_pairing_G1_G2 = 0
for i in range (count):
    P=group.random(G1)
    Q=group.random(G2)
    start = time.perf_counter()
    R = pair(P,Q)
    end = time.perf_counter()
    total_pairing_G1_G2 += end-start
print("total time of pairing e(g_1^a , g_2^b) = ",total_pairing_G1_G2," s.")

total_add_GT = 0
for i in range (count):
    P=group.random(GT)
    Q=group.random(GT)
    start = time.perf_counter()
    R = P * Q
    end = time.perf_counter()
    total_add_GT += end-start
print("total time in G_T of (g^a * g^b) or (g^a + g^b) = ",total_add_GT," s.")

total_exp_GT = 0
for i in range (count):
    P=group.random(GT)
    x = group.random(ZR)
    start = time.perf_counter()
    R = P ** x
    end = time.perf_counter()
    total_exp_GT += end-start
print("total time in G_T of g^a = ",total_exp_GT," s.")

print("==========Testing Plain Elliptic Curve==========")

group = ECGroup(secp256k1)

total_add = 0
for i in range(count):
    P = group.random(G)
    Q = group.random(G)
    start = time.perf_counter()
    R = P * Q
    end = time.perf_counter()
    total_add += end - start
print("total time of P + Q = ", total_add," s.")

total_mul = 0
for i in range(count):
    P = group.random(G)
    x = group.random(ZR)
    start = time.perf_counter()
    Q = P ** x
    end = time.perf_counter()
    total_mul += end - start
print("total time of x * P = ", total_mul," s.")
