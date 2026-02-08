import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html', 
  styleUrls: ['./app.css']    
})
export class AppComponent {
  text: string = '';
  shift: number = 3;
  result: string = '';
  isLoading: boolean = false;

  constructor(private http: HttpClient) {}

  process(mode: 'encrypt' | 'decrypt') {
    if (!this.text) return;

    this.isLoading = true;
    
    // O endereço do Python (Flask)
    const apiUrl = 'http://127.0.0.1:5000/cipher';

    const payload = {
      text: this.text,
      shift: this.shift,
      mode: mode
    };

    this.http.post<any>(apiUrl, payload)
      .subscribe({
        next: (response) => {
          this.result = response.result;
          this.isLoading = false;
        },
        error: (error) => {
          console.error('Erro de conexão:', error);
          this.result = 'Erro: O backend Python está rodando?';
          this.isLoading = false;
        }
      });
  }
}