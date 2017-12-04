#!/bin/bash
echo "python3 verGio.py > outGio.txt..."
python3 verGio.py > outGio.txt
echo "done"
echo "python3 verTanso1.py > outTanso1.txt...(this will take a minute)..."
python3 verTanso1.py > outTanso1.txt
echo "done"
echo "python3 verTanso2.py > outTanso2.txt..."
python3 verTanso2.py > outTanso2.txt
echo "done"
echo "python3 verTanso3.py > outTanso3.txt..."
python3 verTanso3.py > outTanso3.txt
echo "done"
echo "python3 verTanso4.py > outTanso4.txt..."
python3 verTanso4.py > outTanso4.txt
echo "done"
echo "check that files have same size and number of lines:"
wc outGio.txt outTanso1.txt outTanso2.txt outTanso3.txt outTanso4.txt
echo "tempi verGio:"
tail -1 outGio.txt
echo "tempi verTanso1:"
tail -1 outTanso1.txt
echo "tempi verTanso2:"
tail -1 outTanso2.txt
echo "tempi verTanso3:"
tail -1 outTanso3.txt
echo "tempi verTanso4:"
tail -1 outTanso4.txt
