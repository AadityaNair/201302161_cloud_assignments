; 64-bit program to add two single-digit numbers
; By Aaditya M Nair 201302161
; Since 64-bit is backward compatible with 32-bit code 
; * without * any performance loss.
; Here is the same 32-bit code :-)


section .text
    global _start

_start:
    mov eax, 3
    mov ebx, 4
    add eax, ebx

    add eax, '0'
    mov [temp], eax

    mov ecx, temp
    mov edx, 1
    mov ebx, 1
    mov eax, 4
    int 0x80

    mov eax, 1
    int 0x80

segment .bss
    temp resb 1
