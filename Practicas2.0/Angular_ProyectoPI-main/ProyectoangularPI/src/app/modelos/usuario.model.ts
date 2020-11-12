export class usuario{
    constructor(
        public _id:string,
        public carnet: string,
        public nombre: string,
        public apellidos: string,
        public password: string,
        public correo: string
    ){}
}