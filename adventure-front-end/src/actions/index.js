import axios from 'axios';
export const PENDING = 'PENDING';
export const ERROR = 'ERROR';
export const SUCCESS_ADVENTURE = 'SUCCESS_ADVENTURE';
export const SUCCESS_CHAT = 'SUCCESS_CHAT';
export const UPDATING = "UPDATING";

export const createAdventure = () => {
    return (dispatch) => {
        dispatch({ type: PENDING });
        axios
            .get('http://127.0.0.1:8000/api/adv')
            .then(response => {
                dispatch({ type: SUCCESS_ADVENTURE, adventures: response.data })
            })
            .catch(err => {
                dispatch({ type: ERROR, error: 'ERROR FETCHING ADVENTURE' })
            })
    }
}

//pending or updating??
export const moveAdventure = (move) => {
    return dispatch => {
        dispatch({ type: PENDING });
        console.log(move);
        axios
            .post('http://127.0.0.1:8000/api/adv', move)
            .then(response => {
                dispatch({ type: SUCCESS_ADVENTURE, adventure: response.data })
            })
            .catch(() => {
                dispatch({ type: ERROR, error: 'ERROR CREATING MOVE' })
            })
    }
}

export const createChat = (message) => {
    return dispatch => {
        dispatch({ type: PENDING });
        console.log(message);
        axios
            .post('http://127.0.0.1:8000/api/adv', message)
            .then(response => {
                dispatch({ type: SUCCESS_CHAT, chat: response.data })
            })
            .catch(() => {
                dispatch({ type: ERROR, error: 'ERROR CREATING CHAT' })
            })
    }
}
