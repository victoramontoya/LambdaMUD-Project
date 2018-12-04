import { PENDING, ERROR, SUCCESS_CHAT, SUCCESS_ADVENTURE, UPDATING } from '../actions';

const initialState = {
    chat: [],
    adventure: [],
    creatingAdventure: false,
    fetchingAdventure: false,
    creatingChat: false,
    updatingChat: false,
    error: null,
    // chat: {
    //     modal: false,

    // }
}

const adventureReducer = (state = initialState, action) => {
    switch (action.type) {
        case PENDING:
            return Object.assign({}, state, { updatingChat: true });
        case SUCCESS_CHAT:
            return Object.assign({}, state, {
                chat: action.chat,
                updatingChat: false
            });
        case SUCCESS_ADVENTURE:
            return Object.assign({}, state, {
                adventure: action.adventure,
                fetchingAdventure: false
            });
        case ERROR:
            return Object.assign({}, state, {
                error: action.error,
                fetchingAdventure: false
            });
        case UPDATING:
            return Object.assign({}, state, {
                updating: true,
                adventure: action.adventure
            });
        default:
            return state;
    }

}

export default adventureReducer;