import { Component, OnInit } from '@angular/core';
import {Router, ActivatedRoute, Params, RouterLink} from "@angular/router";
import { usuario } from '../modelos/usuario.model';
import { UsuarioService } from '../services/usuario.service';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css'],
  providers: [UsuarioService]
})
export class RegistroComponent implements OnInit {

  public usuario: usuario;
  public status: string;

  constructor(private _route: ActivatedRoute,
    private _router: Router,private servicio: UsuarioService,) { 
      this.usuario = new usuario("",null,"","","","",);
  }

  ngOnInit(): void {
    this.camposVacios();
  }

  crearUsuario(){
    this.servicio.crearUsuario(this.usuario).subscribe(
      Response =>{
        console.log(Response);
        if(Response){
          this.status = 'success';
          this._router.navigate(['/login']);
        }
      }
    )
  }

  camposVacios(){
    
  }
}
