package beak;

import java.util.Scanner;

public class beak6603 {
    // 배열 출력
	static void print(int[] arr, boolean[] visited, int n) {
		for (int i = 0; i < n; i++) {
			if(visited[i]) {
				System.out.print(arr[i] + " ");
			}
		}
		System.out.println();
	}   
    // 1. 백트래킹 구현 
	// 사용 예시 : combination(int[] arr, visited, 0, n, r)
	static void combination(int[] arr, boolean[] visited, int start, int n, int r) {
		if(r == 0) {
			print(arr, visited, n);
			return;
		} 
		
		for(int i = start; i < n; i++) {
			visited[i] = true;
			combination(arr, visited, i + 1, n, r - 1);
			visited[i] = false;
		}
	}
	
	// 2. 재귀 사용
	// 사용 예시 : comb(arr, visited, 0, n, r)
	static void comb(int[] arr, boolean[] visited, int depth, int n, int r) {
		if(r == 0) {
			print(arr, visited, n);
			return;
		}
		
		if(depth == n) {
			return;
		}
		
		visited[depth] = true;
		comb(arr, visited, depth + 1, n, r-1);
		
		visited[depth] = false;	// 빼먹지 않기!
		comb(arr, visited, depth + 1, n, r);
	}
	
	public static void main(String[] args) {
		int n = 8;
		int[] arr = {1, 2, 3, 4, 5, 6, 7, 8};
		boolean[] visited = new boolean[n];
		
		
			//comb(arr, visited, 0, n, i);
		
		
		
			combination(arr, visited, 0, n, 6);
		
	}
	
	 
}
