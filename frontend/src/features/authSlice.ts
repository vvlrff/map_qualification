import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../app/store";

export interface AuthState {
    access_token: string | null;
};

const initialState: AuthState = {
    access_token: null
};

export const authSlice = createSlice({
    name: "auth",
    initialState,
    reducers: {
        setUser: (
            state,
            action: PayloadAction<{ access_token: string }>
        ) => {
            localStorage.setItem(
                "user",
                JSON.stringify({
                    access_token: action.payload.access_token
                })
            );
            state.access_token = action.payload.access_token;
        },
        logout: (state) => {
            localStorage.clear();
            state.access_token = null;
        },
    }
});

export const selectAuth = (state: RootState) => state.auth;

export const { setUser, logout } = authSlice.actions;

export default authSlice.reducer;