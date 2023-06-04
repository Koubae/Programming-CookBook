package com.koubae.model;


import org.json.JSONObject;

public class Task {
    private Long id;
    private String name;
    private String description;
    private boolean completed = false;
    private String created;
    private String updated;

    public Task(String name) {}
    public Task(String name, String description) {}
    public Task(Long id, String name, String description, boolean completed, String created, String updated) {}

    public JSONObject toJSON() {
        JSONObject json = new JSONObject();
        json.put("integer", mSomeInt);
        json.put("string", mSomeString);

        return jo;
    }

}
