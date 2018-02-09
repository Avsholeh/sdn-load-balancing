# Load Balancing in Software Defined Network

Repositori ini merupakan hasil dari penerapan load balancing pada arsitektur Software Defined Network dengan menggunakan beberapa algoritma antara lain: 
  - Agen Based (core/algorithm/agenbased.py)
  - Flow Based (core/algorithm/flowbased.py)
  - Round Robin (core/algoritm/roundrobin.py)

## Agen Based
Modul ini adalah load balancing dengan algoritma least connection menggunakan agen yang berfungsi mendistribusikan jumlah koneksi pada server.

## Flow Based
Modul ini adalah load balancing dengan algoritma least connection menggunakan flow yang tersimpan untuk dijadikan parameter jumlah koneksi pada server.

## Round Robin
Modul ini menggunakan algoritma round robin sebagai metode pemilihan server pada load balancing.

# Instalasi
Modul-modul tersebut merupakan modul yang berjalan pada aplikasi POX. Dimana aplikasi tersebut merupakan SDN-Controller yang menggunakan OpenFlow1.0 sebagai protokol komunikasi dengan OFSwitch. Untuk menjalankan modul tersebut kita harus melakukan clone repositori pada POX-carp dengan cara sebagai berikut:
```
$ git clone https://github.com/noxrepo/pox
```
Setelah itu kita dapat memindahkan/menduplikasikan modul tersebut kedalam direktori POX.
```
$ cp ~/load-balancing/core/algorithm/roundrobin.py ~/pox/ext/roundrobin.py
```

# How-to
Setelah melakukan tahap instalasi kita dapat menjalankan modul tersebut dengan cara sebagai berikut:
```
$ cd pox
$ ./pox.py log.level --DEBUG roundrobin --ip=<virtual-ip> --servers=<list-of-server>
```