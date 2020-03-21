import axios from 'axios'

const hostname = '127.0.0.1';
const port = 5000;
// let host = process.env.NODE_ENV === 'production' ? window.location.host : `${hostname}:${port}`;
let host = `${hostname}:${port}`;

class ApiMorphey {
    constructor() {
        this.http = axios.create({
            baseURL: `http://${host}/api`
        })
    }

    async getSymbols() {
        let response = await this.http.get('/symbols')
            .catch(err => {
                console.log(err)
            });
        return response.data.data;
    }
}

const api = new ApiMorphey();
export default api