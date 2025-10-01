import { Client, Databases, ID } from "node-appwrite";
import "dotenv/config"; // Loads .env locally

console.log("HI");

// Load env vars
const {
    ENDPOINT,
    PROJECT_ID,
    API_KEY,
    DB_ID,
    COLLECTION_ID,
} = process.env;

console.log("Loaded ENV:", {
    ENDPOINT,
    PROJECT_ID,
    API_KEY: API_KEY ? "(set)" : "(notSet)",
    DB_ID,
    COLLECTION_ID,
});

// Export named handler function for Jest import
export async function handler({ req, res }) {
    try {
        // Init Appwrite client
        const client = new Client()
            .setEndpoint(ENDPOINT)
            .setProject(PROJECT_ID)
            .setKey(API_KEY);

        const databases = new Databases(client);

        if (req.method === "GET") {
            // Fetch all documents
            const result = await databases.listDocuments(DB_ID, COLLECTION_ID);
            return res.json(result.documents);
        }

        if (req.method === "POST") {
            // Parse request body
            const data = JSON.parse(req.bodyRaw || "{}");
            if (!data.title) {
                return res.json({ error: "Missing 'title' field" }, 400);
            }

            // Create new document
            const result = await databases.createDocument(
                DB_ID,
                COLLECTION_ID,
                ID.unique(),
                data
            );
            return res.json(result);
        }

        return res.text("Method not allowed", 405);
    } catch (err) {
        console.error("Function Error:", err);
        return res.json({ error: err.message }, 500);
    }
}
